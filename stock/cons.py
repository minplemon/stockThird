#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-21 11:05
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : cons.py
# @Software: PyCharm
import sys
K_LABELS = ['D', 'W', 'M']
K_MIN_LABELS = ['5', '15', '30', '60']
K_TYPE = {'D': 'akdaily', 'W': 'akweekly', 'M': 'akmonthly'}
INDEX_LABELS = ['sh', 'sz', 'hs300', 'sz50', 'cyb', 'zxb', 'zx300', 'zh500']
INDEX_LIST = {'sh': 'sh000001', 'sz': 'sz399001', 'hs300': 'sh000300',
              'sz50': 'sh000016', 'zxb': 'sz399005', 'cyb': 'sz399006',
              'zx300': 'sz399008', 'zh500': 'sh000905'}
DAY_PRICE_URL = '%sapi.finance.%s/%s/?code=%s&type=last'
DAY_PRICE_MIN_URL = '%sapi.finance.%s/akmin?scode=%s&type=%s'
P_TYPE = {'http': 'http://', 'ftp': 'ftp://'}
PAGE_NUM = [40, 60, 80, 100]
DOMAINS = {'sina': 'sina.com.cn', 'sinahq': 'sinajs.cn',
           'ifeng': 'ifeng.com', 'sf': 'finance.sina.com.cn',
           'vsf': 'vip.stock.finance.sina.com.cn',
           'idx': 'www.csindex.com.cn', '163': 'money.163.com',
           'em': 'eastmoney.com', 'sseq': 'query.sse.com.cn',
           'sse': 'www.sse.com.cn', 'szse': 'www.szse.cn',
           'oss': 'file.tushare.org', 'idxip': '115.29.204.48',
           'shibor': 'www.shibor.org', 'mbox': 'www.cbooo.cn',
           'tt': 'gtimg.cn', 'gw': 'gw.com.cn',
           'v500': 'value500.com', 'sstar': 'stock.stockstar.com',
           'dfcf': 'nufm.dfcfw.com'}
FORMAT = lambda x: '%.2f' % x
FORMAT4 = lambda x: '%.4f' % x
HIST_FQ_COLS = ['date', 'open', 'high', 'close', 'low', 'volume', 'amount', 'factor']
HIST_FQ_URL = '%s%s/corp/go.php/vMS_FuQuanMarketHistory/stockid/%s.phtml?year=%s&jidu=%s'
HIST_INDEX_URL = '%s%s/corp/go.php/vMS_MarketHistory/stockid/%s/type/S.phtml?year=%s&jidu=%s'
HIST_FQ_FACTOR_URL = '%s%s/api/json.php/BasicStockSrv.getStockFuQuanData?symbol=%s&type=hfq'
INX_DAY_PRICE_COLUMNS = [
    'date',
    'open',
    'high',
    'close',
    'low',
    'volume',
    'price_change',
    'p_change',
    'ma5',
    'ma10',
    'ma20',
    'v_ma5',
    'v_ma10',
    'v_ma20']
DAY_PRICE_COLUMNS = [
    'date',
    'open',
    'high',
    'close',
    'low',
    'volume',
    'price_change',
    'p_change',
    'ma5',
    'ma10',
    'ma20',
    'v_ma5',
    'v_ma10',
    'v_ma20',
    'turnover']
DAY_TRADING_COLUMNS = [
    'code',
    'symbol',
    'name',
    'changepercent',
    'trade',
    'open',
    'high',
    'low',
    'settlement',
    'volume',
    'turnoverratio',
    'amount',
    'per',
    'pb',
    'mktcap',
    'nmc']
LIVE_DATA_COLS = [
    'name',
    'open',
    'pre_close',
    'price',
    'high',
    'low',
    'bid',
    'ask',
    'volume',
    'amount',
    'b1_v',
    'b1_p',
    'b2_v',
    'b2_p',
    'b3_v',
    'b3_p',
    'b4_v',
    'b4_p',
    'b5_v',
    'b5_p',
    'a1_v',
    'a1_p',
    'a2_v',
    'a2_p',
    'a3_v',
    'a3_p',
    'a4_v',
    'a4_p',
    'a5_v',
    'a5_p',
    'date',
    'time',
    's']
NETWORK_URL_ERROR_MSG = '获取失败，请检查网络.'
TICK_SRCS = ['sn', 'tt', 'nt']
TICK_SRC_ERROR = '数据源代码只能输入sn,tt,nt其中之一'
TICK_PRICE_URL = '%smarket.%s/%s?date=%s&symbol=%s'
TICK_PRICE_URL_TT = '%sstock.%s/data/%s?appn=detail&action=download&c=%s&d=%s'
TICK_PRICE_URL_NT = '%squotes.%s/cjmx/%s/%s/%s.xls'
PAGES = {
    'fd': 'index.phtml',
    'dl': 'downxls.php',
    'jv': 'json_v2.php',
    'cpt': 'newFLJK.php',
    'ids': 'newSinaHy.php',
    'lnews': 'rollnews_ch_out_interface.php',
    'ntinfo': 'vCB_BulletinGather.php',
    'hs300b': '000300cons.xls',
    'hs300w': '000300closeweight.xls',
    'sz50b': '000016cons.xls',
    'dp': 'all_fpya.php',
    '163dp': 'fpyg.html',
    'emxsg': 'JS.aspx',
    '163fh': 'jjcgph.php',
    'newstock': 'vRPD_NewStockIssue.php',
    'zz500b': '000905cons.xls',
    'zz500wt': '000905closeweight.xls',
    't_ticks': 'vMS_tradedetail.php',
    'dw': 'downLoad.html',
    'qmd': 'queryMargin.do',
    'szsefc': 'ShowReport.szse',
    'ssecq': 'commonQuery.do',
    'sinadd': 'cn_bill_download.php',
    'ids_sw': 'SwHy.php',
    'idx': 'index.php',
    'index': 'index.html'}
TICK_COLUMNS = ['time', 'price', 'change', 'volume', 'amount', 'type']
DATA_GETTING_TIPS = '[Getting data:]'
DATA_GETTING_FLAG = '#'
DATA_ROWS_TIPS = '%s rows data found.Please wait for a moment.'
SINA_DAY_PRICE_URL = '%s%s/quotes_service/api/%s/Market_Center.getHQNodeData?num=80&sort=code&asc=0&node=%s&symbol=&_s_r_a=page&page=%s'
LIVE_DATA_URL = '%shq.%s/rn=%s&list=%s'
TODAY_TICKS_PAGE_URL = '%s%s/quotes_service/api/%s/CN_Transactions.getAllPageTime?date=%s&symbol=%s'
KLINE_TT_URL = '%sweb.ifzq.%s/appstock/app/%skline/get?_var=kline_day%s&param=%s,%s,%s,%s,640,%s&r=0.%s'
TODAY_TICKS_URL = '%s%s/quotes_service/view/%s?symbol=%s&date=%s&page=%s'
TODAY_TICK_COLUMNS = ['time', 'price', 'pchange', 'change', 'volume', 'amount', 'type']


PY3 = (sys.version_info[0] >= 3)


def _write_head():
    sys.stdout.write(DATA_GETTING_TIPS)
    sys.stdout.flush()


def _write_console():
    sys.stdout.write(DATA_GETTING_FLAG)
    sys.stdout.flush()


def _code_to_symbol(code):
    '''
        生成symbol代码标志
    '''
    if code in INDEX_LABELS:
        return INDEX_LIST[code]
    else:
        if len(code) != 6:
            return code
        else:
            return 'sh%s' % code if code[:1] in [
                '5', '6', '7'] or code[:2] in ['11', '13'] else 'sz%s' % code


def _code_to_symbol_dgt(code):
    if code in INDEX_LABELS:
        return INDEX_LIST[code]
    else:
        if len(code) != 6:
            return code
        else:
            return '0%s' % code if code[:1] in [
                '5', '6', '7'] else '1%s' % code
