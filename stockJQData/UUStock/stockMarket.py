#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-20 10:00
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : stockMarket.py
# @Software: PyCharm


"""
##   行情数据
###  股票历史交易数据  股票 tick 数据 股票实时数据
参考  https://www.joinquant.com/help/api/help?name=Stock#%E8%8E%B7%E5%8F%96%E8%A1%8C%E6%83%85%E6%95%B0%E6%8D%AE
"""
from jqdatasdk import *
auth('18620668927', 'minpeng123')   # 账号密码认证 可通过注册 聚宽领取 https://www.joinquant.com

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
    股票实时数据
    :param :security: 标的代码， 支持股票、商品期货和股指期货以及包含标的代码的列表。 期货需要使用具体合约代码，不可以使用主力合约和指数合约代码
    :rtype :
    :return:当传入参数为标的代码时，返回tick 对象；当传入包含标的代码的列表则返回一个dict，key是标的代码，value和传入一个字符串的返回值一样
    """
    return get_current_tick('000001.XSHE')