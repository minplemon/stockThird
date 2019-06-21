#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-19 14:51
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : stockBaseInfo.py
# @Software: PyCharm

# 获取股票概况
# 包含股票的上市时间、退市时间、代码、名称、是否是ST等
"""
##   获取标的基本信息
###  get_all_securities - 获取所有标的信息
     get_security_info - 获取单个标的信息
     get_index_stocks - 获取指数成份股
     normalize_code-股票代码格式转化
     get_margincash_stocks - 获取融资标的列表
     get_marginsec_stocks - 获取融券标的列表
     get_extras - 获取基金净值/期货结算价等
     get_locked_shares - 获取限售解禁数据
     get_index_weights -获取指数成份股权重（月度）
参考 https://www.joinquant.com/help/api/help?name=JQData#%E8%8E%B7%E5%8F%96%E6%A0%87%E7%9A%84%E5%9F%BA%E6%9C%AC%E4%BF%A1%E6%81%AF
"""

from jqdatasdk import *
auth('18620668927', 'minpeng123')   # 账号密码认证


def stock_get_all_securities():
    """
    获取平台支持的所有股票数据:获取平台支持的所有股票、基金、指数、期货信息
    :param :types: list: 用来过滤securities的类型, list元素可选: 'stock', 'fund', 'index', 'futures', 'etf', 'lof', 'fja', 'fjb'。types为空时返回所有股票, 不包括基金,指数和期货
            date: 日期, 一个字符串或者 [datetime.datetime]/[datetime.date] 对象, 用于获取某日期还在上市的股票信息. 默认值为 None, 表示获取所有日期的股票信息
    :rtype :pandas.DataFrame
    :return:display_name # 中文名称
            name # 缩写简称
            start_date # 上市日期
            end_date # 退市日期，如果没有退市则为2200-01-01
            type # 类型，stock(股票)
    : otherfun
                #将所有股票列表转换成数组
                stocks = list(get_all_securities(['stock']).index)

                #获得所有指数列表
                get_all_securities(['index'])

                #获得所有基金列表
                df = get_all_securities(['fund'])

                #获取所有期货列表
                get_all_securities(['futures'])

                #获得etf基金列表
                df = get_all_securities(['etf'])
                #获得lof基金列表
                df = get_all_securities(['lof'])
                #获得分级A基金列表
                df = get_all_securities(['fja'])
                #获得分级B基金列表
                df = get_all_securities(['fjb'])

                #获得2015年10月10日还在上市的所有股票列表
                get_all_securities(date='2015-10-10')
                #获得2015年10月10日还在上市的 etf 和 lof 基金列表
                get_all_securities(['etf', 'lof'], '2015-10-10')
    """
    return get_all_securities(types=['stock'], date=None)



def stock_get_security_info():
    """
    获取单支股票的信息 :获取股票/基金/指数的信息
    :param : code: 证券代码
    :rtype :Security 一个对象
    :return:display_name # 中文名称
            name # 缩写简称
            start_date # 上市日期, [datetime.date] 类型
            end_date # 退市日期， [datetime.date] 类型, 如果没有退市则为2200-01-01
            type # 类型，stock(股票)，index(指数)，etf(ETF基金)，fja（分级A），fjb（分级B）
            parent # 分级基金的母基金代码
    """

    return get_security_info('502050.XSHG')

def stock_get_index_stocks():
    """
    获取一个指数给定日期在平台可交易的成分股列表
    :param  :index_symbol, 指数代码
            date: 查询日期, 一个字符串(格式类似’2015-10-15’)或者[datetime.date]/[datetime.datetime]对象, 可以是None, 使用默认日期. 这个默认日期在回测和研究模块上有点差别:
    :沪深指数列表 :https://www.joinquant.com/help/api/help?name=index#%E6%B2%AA%E6%B7%B1%E6%8C%87%E6%95%B0%E5%88%97%E8%A1%A8
    :rtype : list
    :return:
    """
    return get_index_stocks('000300.XSHG')


def stock_get_margincash_stocks():
    """
    获取融资标的列表
    :param :date:默认为None,不指定时返回上交所、深交所最近一次披露的的可融资标的列表的list
    :rtype : list
    :return:返回指定日期上交所、深交所披露的的可融资标的列表的list
    """
    return get_margincash_stocks()


def stock_get_marginsec_stocks():
    """
    获取融券标的列表
    :param :date:默认为None,不指定时返回上交所、深交所最近一次披露的的可融券标的列表的list
    :rtype : list
    :return:返回指定日期上交所、深交所披露的的可融券标的列表的list
    """
    return get_marginsec_stocks()


def stock_get_locked_shares():
    """
    获取指定日期区间内的限售解禁数据
    :param :stock_list: 一个股票代码的 list
            start_date: 开始日期
            end_date: 结束日期
            forward_count: 交易日数量， 可以与 start_date 同时使用， 表示获取 start_date 到 forward_count 个交易日区间的数据
    :rtype :pandas.DataFrame
    :return:day: 解禁日期
            code: 股票代码
            num: 解禁股数
            rate1: 解禁股数/总股本
            rate2: 解禁股数/总流通股本
    """
    return get_locked_shares(stock_list=['000001.XSHE', '000002.XSHE'], start_date='2018-08-01', forward_count=500)

def stock_get_index_weights():
    """
    获取指数成份股权重（月度）
    获取指数成份股给定日期的权重数据，每月更新一次，请点击指数列表查看指数信息
    :指数列表 https://www.joinquant.com/help/api/help?name=index#%E6%B2%AA%E6%B7%B1%E6%8C%87%E6%95%B0%E5%88%97%E8%A1%A8
    :param :index_id: 代表指数的标准形式代码， 形式：指数代码.交易所代码，例如"000001.XSHG"。
            date: 查询权重信息的日期，形式："%Y-%m-%d"，例如"2018-05-03"；
    :rtype :pandas.DataFrame
    :return:查询到对应日期，且有权重数据，返回 pandas.DataFrame， code(股票代码)，display_name(股票名称), date(日期), weight(权重)；
            查询到对应日期，且无权重数据， 返回距离查询日期最近日期的权重信息；
            找不到对应日期的权重信息， 返回距离查询日期最近日期的权重信息
    """
    return get_index_weights(index_id="000001.XSHG", date="2018-05-09")



def stock_get_extras():
    """
    获取基金净值/期货结算价等
    :param :info: ['is_st', 'acc_net_value', 'unit_net_value', 'futures_sett_price', 'futures_positions'] 中的一个
            指定info字段	返回信息
            is_st	是否是ST，是则返回 True，否则返回 False
            acc_net_value	基金累计净值
            unit_net_value	基金单位净值
            futures_sett_price	期货结算价
            futures_positions	期货持仓量
            adj_net_value	场外基金的复权净值
            security_list: 股票列表

            start_date/end_date: 开始结束日期, 同 [get_price]

            df: 返回[pandas.DataFrame]对象还是一个dict, 同 [history]

            count: 数量, 与 start_date 二选一, 不可同时使用, 必须大于 0. 表示取 end_date 往前的 count 个交易日的数据
    :rtype : pandas.DataFrame
    :return:
    """
    return get_extras('is_st', ['000001.XSHE', '000018.XSHE'], start_date='2013-12-01', end_date='2013-12-03')


def stock_get_mtss():
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

ss = get_index_weights(index_id="000001.XSHG", date="2018-05-09")
print(ss)