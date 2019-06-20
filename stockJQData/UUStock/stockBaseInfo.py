#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-20 10:07
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : stockBaseInfo.py
# @Software: PyCharm

"""
##   股票基本数据
###  获取单支股票的信息 获取平台支持的所有股票数据 查询股票所属行业
参考  https://www.joinquant.com/help/api/help?name=Stock#%E8%8E%B7%E5%8F%96%E8%82%A1%E7%A5%A8%E6%A6%82%E5%86%B5
"""
from jqdatasdk import *
auth('18620668927', 'minpeng123')   # 账号密码认证 可通过注册 聚宽领取 https://www.joinquant.com


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