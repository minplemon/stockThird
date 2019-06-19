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
from jqdatasdk import *
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

def uu_get_extras():
    """
    得到多只股票在一段时间是否是ST
    :param :info: ‘is_st’
            security_list: 股票列表
            start_date/end_date: 开始结束日期, 同[get_price]
            df: 返回[pandas.DataFrame]对象还是一个dict
    :rtype : pandas.DataFrame
    :return:
    """
    return get_extras('is_st', ['000001.XSHE', '000018.XSHE'], start_date='2013-12-01', end_date='2013-12-03')


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
