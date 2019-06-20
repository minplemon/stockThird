#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-19 14:20
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : UUStockDiagnoseData.py
# @Software: PyCharm

## 诊股详情
from jqdatasdk import *
import logging as log
auth('18620668927', 'minpeng123')   # 账号密码认证

def uu_get_security_info():
    """
    获取单支股票的信息
    :param : code: 证券代码
    :rtype :Security 一个对象
    :return:display_name # 中文名称
            name # 缩写简称
            start_date # 上市日期, [datetime.date] 类型
            end_date # 退市日期， [datetime.date] 类型, 如果没有退市则为2200-01-01
            type # 类型，stock(股票)，index(指数)，etf(ETF基金)，fja（分级A），fjb（分级B）
            parent # 分级基金的母基金代码
    """

    return get_security_info('000001.XSHE')

def uu_get_all_securities():
    """
    获取平台支持的所有股票数据
    :param :types：默认为stock，这里请在使用时注意防止未来函数。
            date: 日期, 一个字符串或者 [datetime.datetime]/[datetime.date] 对象, 用于获取某日期还在上市的股票信息. 默认值为 None, 表示获取所有日期的股票信息
    :rtype :pandas.DataFrame
    :return:display_name # 中文名称
            name # 缩写简称
            start_date # 上市日期
            end_date # 退市日期，如果没有退市则为2200-01-01
            type # 类型，stock(股票)
    """
    return get_all_securities(types=['stock'], date=None)

def uu_get_industry():
    """
    查询股票所属行业
    :param :security：标的代码，类型为字符串，形式如"000001.XSHE"；或为包含标的代码字符串的列表，形如["000001.XSHE", "000002.XSHE"]
            date：查询的日期。类型为字符串，形如"2018-06-01"或"2018-06-01 09:00:00"；或为datetime.datetime对象和datetime.date。注意传入对象的时分秒将被忽略
    :rtype :dict
    :return:
    """
    return get_industry("600519.XSHG",date="2018-06-01")

def uu_get_mtss():
    """
    获取一只或者多只股票在一个时间段内的融资融券信息
    :param :security_list: 一只股票代码或者一个股票代码的 list
            start_date: 开始日期, 一个字符串或者 datetime.datetime/datetime.date 对象
            end_date: 结束日期, 一个字符串或者 datetime.date/datetime.datetime对象
            fields: 字段名或者 list, 可选. 默认为 None, 表示取全部字段, 各字段含义如下：
                字段名	含义
                date	日期
                sec_code	股票代码
                fin_value	融资余额(元）
                fin_buy_value	融资买入额（元）
                fin_refund_value	融资偿还额（元）
                sec_value	融券余量（股）
                sec_sell_value	融券卖出量（股）
                sec_refund_value	融券偿还股（股）
                fin_sec_value	融资融券余额（元）
    :rtype :pandas.DataFrame
    :return:
    """
    return get_mtss('000001.XSHE', '2016-01-01', '2016-04-01')

def uu_get_index_stocks():
    """
    获取一个指数给定日期在平台可交易的成分股列表
    :param  :index_symbol, 指数代码
            date: 查询日期, 一个字符串(格式类似’2015-10-15’)或者[datetime.date]/[datetime.datetime]对象, 可以是None, 使用默认日期. 这个默认日期在回测和研究模块上有点差别:
    :沪深指数列表 :https://www.joinquant.com/help/api/help?name=index#%E6%B2%AA%E6%B7%B1%E6%8C%87%E6%95%B0%E5%88%97%E8%A1%A8
    :rtype : list
    :return:
    """
    return get_index_stocks('000300.XSHG')

def uu_get_industry_stocks():
    """
    获取在给定日期一个行业板块的所有股票，行业分类列表见数据页面-行业数据。
    :param :industry_code: 行业编码
            date: 查询日期, 一个字符串(格式类似’2015-10-15’)或者[datetime.date]/[datetime.datetime]对象, 可以是None, 使用默认日期. 这个默认日期在回测和研究模块上有点差别:
    :行业列 : https://www.joinquant.com/data/dict/plateData#%E8%A1%8C%E4%B8%9A%E7%B1%BB
    :rtype : list
    :return:
    """
    return get_industry_stocks('I64')

def uu_get_concept_stocks():
    """
    获取在给定日期一个概念板块的所有股票，概念分类列表见数据页面-概念数据。
    :param :industry_code: 行业编码
            date: 查询日期, 一个字符串(格式类似’2015-10-15’)或者[datetime.date]/[datetime.datetime]对象, 可以是None, 使用默认日期. 这个默认日期在回测和研究模块上有点差别:
    :概念列 : https://www.joinquant.com/data/dict/plateData#%E6%A6%82%E5%BF%B5%E6%9D%BF%E5%9D%97
    :rtype : list
    :return:
    """
    return get_concept_stocks('GN036')

def uu_get_industry():
    """
    查询股票所属行业
    :param :security：标的代码，类型为字符串，形式如"000001.XSHE"；或为包含标的代码字符串的列表，形如["000001.XSHE", "000002.XSHE"]
            date：查询的日期。类型为字符串，形如"2018-06-01"或"2018-06-01 09:00:00"；或为datetime.datetime对象和datetime.date。注意传入对象的时分秒将被忽略
    :概念板块 : https://www.joinquant.com/data/dict/plateData#%E6%A6%82%E5%BF%B5%E6%9D%BF%E5%9D%97
    :rtype :dict
    :return:
    """
    return get_industry("600519.XSHG",date="2018-06-01")

def uu_get_fundamentals():
    """
    :表名 : valuation 市值数据
            balance 资产负债数据
            cash_flow 现金流数据
            income 利润数据
            indicator 财务指标数据
            bank_indicator 银行业专项指标
            security_indicator 券商业专项指标
            insurance_indicator 保险业专项指标
    :param :query_object: 一个sqlalchemy.orm.query.Query对象, 可以通过全局的query函数获取Query对象，query简易教程。
            date: 查询日期, 一个字符串(格式类似’2015-10-15’)或者[datetime.date]/[datetime.datetime]对象, 可以是None, 使用默认日期. 这个默认日期在回测和研究模块上有点差别:
    :return:
    """

    # 查询'000001.XSHE'的所有市值数据, 时间是2015-10-15
    q = query(
        valuation
    ).filter(
        valuation.code == '000001.XSHE'
    )
    df = get_fundamentals(q, '2015-10-15')
    # 打印出总市值
    log.info(df['market_cap'][0])
    return df


def uu_get_price():
    """
    (可拿到当天数据)
    获取股票历史交易数据，可以通过参数设置获取日k线、分钟k线数据。获取数据的基本属性如下
    :param :security: 一支股票代码或者一个股票代码的list
            start_date: 字符串或者[datetime.datetime]/[datetime.date]对象, 开始时间, 默认是’2015-01-01’. 注意:
            当取分钟数据时, 时间可以精确到分钟, 比如: 传入 datetime.datetime(2015, 1, 1, 10, 0, 0) 或者 '2015-01-01 10:00:00'.
            当取分钟数据时, 如果只传入日期, 则日内时间是当日的 00:00:00.
            当取天数据时, 传入的日内时间会被忽略
            end_date: 格式同上, 结束时间, 默认是’2015-12-31’, 包含此日期. 注意: 当取分钟数据时, 如果 end_date 只有日期, 则日内时间等同于 00:00:00, 所以返回的数据是不包括 end_date 这一天的.
            frequency: 单位时间长度, 几天或者几分钟, 现在支持’Xd’,’Xm’, ‘daily’(等同于’1d’), ‘minute’(等同于’1m’), X是一个正整数, 分别表示X天和X分钟(不论是按天还是按分钟回测都能拿到这两种单位的数据), 注意, 当X > 1时, field只支持[‘open’, ‘close’, ‘high’, ‘low’, ‘volume’, ‘money’]这几个标准字段. 默认值是daily
            fields: 字符串list, 选择要获取的行情数据字段, 默认是None(表示['open','close','high','low','volume', 'money']这几个标准字段), 支持属性里面的所有基本属性.
            skip_paused: 是否跳过停牌的时间, 如果不跳过, 停牌时会使用停牌前的数据填充(具体请看[SecurityUnitData]的paused属性), 但要注意:

            默认为 False
            当 skip_paused 是 True 时, 只能取一只股票的信息
    :rtype : pandas.DataFrame
    :return:open 时间段开始时价格
            close 时间段结束时价格
            low 最低价
            high 最高价
            volume 成交的股票数量
            money 成交的金额
            factor 前复权因子, 我们提供的价格都是前复权后的, 但是利用这个值可以算出原始价格, 方法是价格除以factor, 比如: close/factor
            high_limit 涨停价
            low_limit 跌停价
            avg 这段时间的平均价, 等于money/volume
            pre_close 前一个单位时间结束时的价格, 按天则是前一天的收盘价, 按分钟这是前一分钟的结束价格
            paused 布尔值, 这只股票是否停牌, 停牌时open/close/low/high/pre_close依然有值,都等于停牌前的收盘价, volume=money=0
    """
    return get_price('000001.XSHE', start_date='2019-06-19', end_date='2019-06-21', frequency='1m',
               fields=['open', 'close','low','high','volume','money','factor','high_limit','low_limit','avg','pre_close','paused'])


def uu_get_ticks():
    """
    获取股票 tick 数据 (历史数据)
    :param :security: 股票代码或期货代码
            end_dt: 结束日期
            start_dt: 开始日期, 与count参数二选一
            count: 取出指定时间区间内前多少条的tick数据, 与start_dt参数二选一
            fields: 选择要获取的行情数据字段，默认为["time", "current", "high", "low", "volume", "money"]
    :rtype : numpy.ndarray
    :return:    字段名	说明	字段类型
                time	时间	float
                current	当前价	float
                high	当日最高价	float
                low	当日最低价	float
                volume	累计成交量	float
                money	累计成交额	float
                a1_v~a5_v	五档卖量	float
                a1_p~a5_p	五档卖价	float
                b1_v~b5_v	五档买量	float
                b1_p~b5_p	五档买价	float
    """
    return get_ticks("000001.XSHE",start_dt="2019-06-19", end_dt="2019-06-21")


def uu_get_current_tick():
    """
    :param :security: 标的代码， 支持股票、商品期货和股指期货以及包含标的代码的列表。 期货需要使用具体合约代码，不可以使用主力合约和指数合约代码
    :rtype :
    :return:当传入参数为标的代码时，返回tick 对象；当传入包含标的代码的列表则返回一个dict，key是标的代码，value和传入一个字符串的返回值一样
    """
    return get_current_tick('000001.XSHE')