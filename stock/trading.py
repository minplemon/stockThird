#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-21 11:01
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : trading.py
# @Software: PyCharm


import time
import json
import lxml.html
from lxml import etree
import pandas as pd
import numpy as np
from util import dateu as du
import re
from pandas.compat import StringIO
from stock import cons as ct
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib3 import urlopen, Request

# 获取某只股票的历史数据


def get_hist_data(
        code=None,
        start=None,
        end=None,
        ktype='D',
        retry_count=3,
        pause=0.001):
    """
        获取分笔数据
    Parameters
    ------
        code:string
                  股票代码 e.g. 600848
        date:string
                  日期 format: YYYY-MM-DD
        retry_count : int, 默认 3
                  如遇网络等问题重复执行的次数
        pause : int, 默认 0
                 重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
        src : 数据源选择，可输入sn(新浪)、tt(腾讯)、nt(网易)，默认sn
     return
     -------
        DataFrame 当日所有股票交易数据(DataFrame)
              属性:成交时间、成交价格、价格变动，成交手、成交金额(元)，买卖类型
    """
    symbol = ct._code_to_symbol(code)
    url = ''
    if ktype.upper() in ct.K_LABELS:
        url = ct.DAY_PRICE_URL % (ct.P_TYPE['http'], ct.DOMAINS['ifeng'],
                                  ct.K_TYPE[ktype.upper()], symbol)
    elif ktype in ct.K_LABELS:
        url = ct.DAY_PRICE_MIN_URL % (ct.P_TYPE['http'], ct.DOMAINS['ifeng'],
                                      symbol, ktype)
    else:
        raise TypeError('ktype input error.')
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            request = Request(url)
            lines = urlopen(request, timeout=10).read()
            if len(lines) < 15:  # no data
                return None
        except Exception as e:
            print(e)
        else:
            # 将json字符串编码成Python对象
            js = json.loads(lines.decode('utf-8') if ct.PY3 else lines)
            cols = []
            if (code in ct.INDEX_LABELS) & (ktype.upper() in ct.K_LABELS):
                cols = ct.INX_DAY_PRICE_COLUMNS
            else:
                cols = ct.DAY_PRICE_COLUMNS
            if len(js['record'][0]) == 14:
                cols = ct.INX_DAY_PRICE_COLUMNS
            df = pd.DataFrame(js['record'], columns=cols)
            if ktype.upper() in ct.K_LABELS:
                df = df.applymap(lambda x: x.replace(u',', u''))  # 去逗号
                df[df == ''] = 0
            for col in cols[1:]:
                df[col] = df[col].astype(float)  # 设置浮点型
            if start is not None:
                df = df[df.date >= start]
            if end is not None:
                df = df[df.date <= end]
            if (code in ct.INDEX_LABELS) & (ktype in ct.K_MIN_LABELS):
                df = df.drop('turnover', axis=1)  # 删除列turnover
            df = df.set_index('date')  # 设置date为索引
            df = df.sort_index(ascending=False)  # 降序ascending= False
            return df
        raise IOError(ct.NETWORK_URL_ERROR_MSG)


def get_tick_data(code=None, date=None, retry_count=3, pause=0.001, src='sn'):
    """
            获取分笔数据
        Parameters
        ------
            code:string
                      股票代码 e.g. 600848
            date:string
                      日期 format: YYYY-MM-DD
            retry_count : int, 默认 3
                      如遇网络等问题重复执行的次数
            pause : int, 默认 0
                     重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
            src : 数据源选择，可输入sn(新浪)、tt(腾讯)、nt(网易)，默认sn
         return
         -------
            DataFrame 当日所有股票交易数据(DataFrame)
                  属性:成交时间、成交价格、价格变动，成交手、成交金额(元)，买卖类型
        """
    if (src.strip() not in ct.TICK_SRCS):
        print(ct.TICK_SRC_ERROR)
        return None
    symbol = ct._code_to_symbol(code)
    symbol_dgt = ct._code_to_symbol_dgt(code)
    datestr = date.replace('-', '')
    url = {
        ct.TICK_SRCS[0]: ct.TICK_PRICE_URL % (ct.P_TYPE['http'], ct.DOMAINS['sf'],
                                              ct.PAGES['dl'], date, symbol),
        ct.TICK_SRCS[1]: ct.TICK_PRICE_URL_TT % (ct.P_TYPE['http'], ct.DOMAINS['tt'],
                                                 ct.PAGES['idx'], symbol, datestr),
        ct.TICK_SRCS[2]: ct.TICK_PRICE_URL_NT % (ct.P_TYPE['http'], ct.DOMAINS['163'],
                                                 date[0:4], datestr, symbol_dgt)
    }
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            if src == ct.TICK_SRCS[2]:
                df = pd.read_excel(url[src])
                df.columns = ct.TICK_COLUMNS
            else:
                re = Request(url[src])
                lines = urlopen(re, timeout=10).read()
                lines = lines.decode('GBK')
                if len(lines) < 20:
                    return None
                df = pd.read_table(StringIO(lines), names=ct.TICK_COLUMNS,
                                   skiprows=[0])
        except Exception as e:
            print(e)
        else:
            return df
    raise IOError(ct.NETWORK_URL_ERROR_MSG)


def get_today_all():
    """
        一次性获取最近一个日交易日所有股票的交易数据
    return
    -------
      DataFrame
           属性：代码，名称，涨跌幅，现价，开盘价，最高价，最低价，最日收盘价，成交量，换手率，成交额，市盈率，市净率，总市值，流通市值
    """
    ct._write_head()
    df = _parsing_dayprice_json('hs_a', 1)
    if df is not None:
        for i in range(2, ct.PAGE_NUM[1]):
            newdf = _parsing_dayprice_json('hs_a', i)
            df = df.append(newdf, ignore_index=True)
    df = df.append(_parsing_dayprice_json('shfxjs', 1),
                   ignore_index=True)
    return df


def _parsing_dayprice_json(types=None, page=1):
    """
           处理当日行情分页数据，格式为json
     Parameters
     ------
        pageNum:页码
     return
     -------
        DataFrame 当日所有股票交易数据(DataFrame)
    """
    ct._write_console()
    request = Request(
        ct.SINA_DAY_PRICE_URL %
        (ct.P_TYPE['http'],
         ct.DOMAINS['vsf'],
         ct.PAGES['jv'],
         types,
         page))
    text = urlopen(request, timeout=10).read()
    if text == 'null':
        return None
    reg = re.compile(r'\,(.*?)\:')
    text = reg.sub(r',"\1":', text.decode('gbk') if ct.PY3 else text)
    text = text.replace('"{symbol', '{"symbol')
    text = text.replace('{symbol', '{"symbol"')
    if ct.PY3:
        jstr = json.dumps(text)
    else:
        jstr = json.dumps(text, encoding='GBK')
    js = json.loads(jstr)
    df = pd.DataFrame(pd.read_json(js, dtype={'code': object}),
                      columns=ct.DAY_TRADING_COLUMNS)
    df = df.drop('symbol', axis=1)
    #     df = df.ix[df.volume > 0]
    return df


def get_realtime_quotes(symbols=None):
    """
        获取实时交易数据 getting real time quotes data
       用于跟踪交易情况（本次执行的结果-上一次执行的数据）
    Parameters
    ------
        symbols : string, array-like object (list, tuple, Series).

    return
    -------
        DataFrame 实时交易数据
              属性:0：name，股票名字
            1：open，今日开盘价
            2：pre_close，昨日收盘价
            3：price，当前价格
            4：high，今日最高价
            5：low，今日最低价
            6：bid，竞买价，即“买一”报价
            7：ask，竞卖价，即“卖一”报价
            8：volumn，成交量 maybe you need do volumn/100
            9：amount，成交金额（元 CNY）
            10：b1_v，委买一（笔数 bid volume）
            11：b1_p，委买一（价格 bid price）
            12：b2_v，“买二”
            13：b2_p，“买二”
            14：b3_v，“买三”
            15：b3_p，“买三”
            16：b4_v，“买四”
            17：b4_p，“买四”
            18：b5_v，“买五”
            19：b5_p，“买五”
            20：a1_v，委卖一（笔数 ask volume）
            21：a1_p，委卖一（价格 ask price）
            ...
            30：date，日期；
            31：time，时间；
    """
    symbols_list = ''
    if isinstance(
            symbols,
            list) or isinstance(
            symbols,
            set) or isinstance(
                symbols,
            pd.Series):
        for code in symbols:
            symbols_list += ct._code_to_symbol(code) + ','
    else:
        symbols_list = ct._code_to_symbol(symbols)
    symbols_list = symbols_list[:1] if len(symbols) > 8 else symbols_list
    request = Request(
        ct.LIVE_DATA_URL %
        (ct.P_TYPE['http'],
         ct.DOMAINS['sinahq'],
         _random(),
         symbols_list))
    text = urlopen(request, timeout=10).read()
    text = text.decode('GBK')
    reg = re.compile(r'\="(.*?)\";')
    data = reg.findall(text)
    regSym = re.compile(r'(?:sh|sz)(.*?)\=')
    syms = regSym.findall(text)
    data_list = []
    syms_list = []
    for index, row in enumerate(data):
        if len(row) > 1:
            data_list.append([astr for astr in row.split(',')])
            syms_list.append(syms[index])
    if len(syms_list) == 0:
        return None
    df = pd.DataFrame(data_list, columns=ct.LIVE_DATA_COLS)
    df = df.drop('s', axis=1)
    df['code'] = syms_list
    ls = [cls for cls in df.columns if '_v' in cls]
    for txt in ls:
        df[txt] = df[txt].map(lambda x: x[:-2])
    return df


def get_h_data(code, start=None, end=None, autype='qfq', index=False,
               retry_count=3, pause=0.001, drop_factor=True):
    '''
    获取历史复权数据
    Parameters
    ------
      code:string
                  股票代码 e.g. 600848
      start:string
                  开始日期 format：YYYY-MM-DD 为空时取当前日期
      end:string
                  结束日期 format：YYYY-MM-DD 为空时取去年今日
      autype:string
                  复权类型，qfq-前复权 hfq-后复权 None-不复权，默认为qfq
      retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数
      pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
      drop_factor : bool, 默认 True
                是否移除复权因子，在分析过程中可能复权因子意义不大，但是如需要先储存到数据库之后再分析的话，有该项目会更加灵活
    return
    -------
      DataFrame
          date 交易日期 (index)
          open 开盘价
          high  最高价
          close 收盘价
          low 最低价
          volume 成交量
          amount 成交金额
    '''

    start = du.today_last_year() if start is None else start
    end = du.today() if end is None else end
    qs = du.get_quarts(start, end)
    qt = qs[0]
    ct._write_head()
    data = _parse_fq_data(_get_index_url(index, code, qt), index,
                          retry_count, pause)
    if data is None:
        data = pd.DataFrame()
    if len(qs) > 1:
        for d in range(1, len(qs)):
            qt = qs[d]
            ct._write_console()
            df = _parse_fq_data(_get_index_url(index, code, qt), index,
                                retry_count, pause)
            if df is None:  # 可能df为空，退出循环
                break
            else:
                data = data.append(df, ignore_index=True)
    if len(data) == 0 or len(
            data[(data.date >= start) & (data.date <= end)]) == 0:
        return pd.DataFrame()
    data = data.drop_duplicates('date')
    if index:
        data = data[(data.date >= start) & (data.date <= end)]
        data = data.set_index('date')
        data = data.sort_index(ascending=False)
        return data
    if autype == 'hfq':
        if drop_factor:
            data = data.drop('factor', axis=1)
        data = data[(data.date >= start) & (data.date <= end)]
        for label in ['open', 'high', 'close', 'low']:
            data[label] = data[label].map(ct.FORMAT)
            data = data.set_index('date')
            data = data.sort_index(ascending=False)  # ascending=False 倒叙
            data = data.astype(float)
            return data


def _parse_fq_data(url, index, retry_count, pause):
    for _ in range(retry_count):
        try:
            request = Request(url)
            text = urlopen(request, timeout=10).read()
            text = text.decode('GBK')
            html = lxml.html.parse(StringIO(text))
            res = html.xpath('//table[@id=\"FundHoldSharesTable\"]')
            if ct.PY3:
                sarr = [etree.tostring(node).decode('utf-8') for node in res]
            else:
                sarr = [etree.tostring(node) for node in res]
            sarr = ''.join(sarr)
            if sarr == '':
                return None
            df = pd.read_html(sarr, skiprows=[0, 1])[0]
            if len(df) == 0:
                return pd.DataFrame()
            if index:
                df.columns = ct.HIST_FQ_COLS[0:7]
            else:
                df.columns = ct.HIST_FQ_COLS
            if df['date'].dtypes == np.object:
                df['date'] = pd.to_datetime(df['date'])
            df = df.drop_duplicates('date')
        except ValueError as e:
            # 时间较早，已经读不到数据
            return None
        except Exception as e:
            print(e)
        else:
            return df
    raise IOError(ct.NETWORK_URL_ERROR_MSG)

def get_today_ticks(code= None,retry_count=3,pause=0.001):
    """
        获取当日分笔明细数据
    Parameters
    ------
        code:string
                  股票代码 e.g. 600848
        retry_count : int, 默认 3
                  如遇网络等问题重复执行的次数
        pause : int, 默认 0
                 重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
     return
     -------
        DataFrame 当日所有股票交易数据(DataFrame)
              属性:成交时间、成交价格、价格变动，成交手、成交金额(元)，买卖类型
    """
    if code is None or len(code) != 6:
        return None
    symbol = ct._code_to_symbol(code)
    date = du.today()
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            request = Request(ct.TODAY_TICKS_PAGE_URL%(ct.P_TYPE['http'],
                                                       ct.DOMAINS['vsf'],
                                                       ct.PAGES['jv'],
                                                       date,symbol))
            data_str = urlopen(request, timeout=10).read()
            data_str = data_str.decode('GBK')
            data_str = data_str[1:-1]
            data_str = eval(data_str, type('Dummy', (dict,),
                                           dict(__getitem__=lambda s, n: n))())
            data_str = json.dumps(data_str)
            data_str = json.loads(data_str)
            pages = len(data_str['detailPages'])
            data = pd.DataFrame()
            ct._write_head()
            for pNo in range(1, pages+1):
                data = data.append(_today_ticks(symbol, date, pNo,
                                                retry_count, pause), ignore_index=True)
        except Exception as er:
            print(str(er))
        else:
            return data
    raise IOError(ct.NETWORK_URL_ERROR_MSG)





    return None

def _today_ticks(symbol,tdate,pageNo,retry_count,pause):
    ct._write_console()
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            html = lxml.html.parse(ct.TODAY_TICKS_URL% (ct.P_TYPE['http'],
                                                        ct.DOMAINS['vsf'],
                                                        ct.PAGES['t_ticks'],
                                                        symbol,tdate,pageNo))
            res = html.xpath('//table[@id=\"datatbl\"]/tbody/tr')
            if ct.PY3:
                sarr = [etree.tostring(node).decode('utf-8') for node in res]
            else:
                sarr = [etree.tostring(node) for node in res]
            sarr = ''.join(sarr)
            sarr = '<table>%s</table>'%sarr
            sarr = sarr.replace('--', '0')
            df = pd.read_html(StringIO(sarr), parse_dates=False)[0]
            df.columns = ct.TODAY_TICK_COLUMNS
            df['pchange'] = df['pchange'].map(lambda x: x.replace('%', ''))
        except Exception as e:
            print(e)
        else:
            return df
    raise IOError(ct.NETWORK_URL_ERROR_MSG)






    return None




def _get_index_url(index, code, qt):
    if index:
        url = ct.HIST_INDEX_URL % (ct.P_TYPE['http'], ct.DOMAINS['vsf'],
                                   code, qt[0], qt[1])
    else:
        url = ct.HIST_FQ_URL % (ct.P_TYPE['http'], ct.DOMAINS['vsf'],
                                code, qt[0], qt[1])
    return url


def _random(n=13):
    from random import randint
    start = 10**(n - 1)
    end = (10**n) - 1
    return str(randint(start, end))
