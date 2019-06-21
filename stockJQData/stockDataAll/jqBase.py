#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-20 10:43
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : jqBase.py
# @Software: PyCharm

"""
##   查询当日剩余可调用条数
###   get_query_count() 查询当日剩余可调用条数
      normalize_code-股票代码格式转化
参考  https://www.joinquant.com/help/api/help?name=JQData#%E7%99%BB%E5%BD%95JQData
"""
from jqdatasdk import *
auth('18620668927', 'minpeng123')   # 账号密码认证 可通过注册 聚宽领取 https://www.joinquant.com

def stock_get_query_count():
    """
    :rtype : dict
    :return:字段名	说明
            total	当日可调用数据总条数
            spare	当日剩余可调用条数
    """
    return get_query_count()

def stock_normalize_code():
    """
    股票代码格式转化
    将其他形式的股票代码转换为jqdatasdk函数可用的股票代码形式。 仅适用于A股市场股票代码以及基金代码,支持传入单只股票或一个股票list 示例
    :return:['000001.XSHE', '000001.XSHE', '000001.XSHE', '000001.XSHE', '000001.XSHE']
    """
    return normalize_code(['000001', 'SZ000001', '000001SZ', '000001.sz', '000001.XSHE'])
