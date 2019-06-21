#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-19 14:53
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : stockClassifyInfo.py
# @Software: PyCharm

# 股票分类信息
# 获取指数成份股，或者行业成份股
from jqdatasdk import *
auth('18620668927', 'minpeng123')   # 账号密码认证



def stock_get_industry_stocks():
    """
    获取在给定日期一个行业板块的所有股票，行业分类列表见数据页面-行业数据。
    :param :industry_code: 行业编码
            date: 查询日期, 一个字符串(格式类似’2015-10-15’)或者[datetime.date]/[datetime.datetime]对象, 可以是None, 使用默认日期. 这个默认日期在回测和研究模块上有点差别:
    :行业列 : https://www.joinquant.com/data/dict/plateData#%E8%A1%8C%E4%B8%9A%E7%B1%BB
    :rtype : list
    :return:
    """
    return get_industry_stocks('I64')

def stock_get_concept_stocks():
    """
    获取在给定日期一个概念板块的所有股票，概念分类列表见数据页面-概念数据。
    :param :industry_code: 行业编码
            date: 查询日期, 一个字符串(格式类似’2015-10-15’)或者[datetime.date]/[datetime.datetime]对象, 可以是None, 使用默认日期. 这个默认日期在回测和研究模块上有点差别:
    :概念列 : https://www.joinquant.com/data/dict/plateData#%E6%A6%82%E5%BF%B5%E6%9D%BF%E5%9D%97
    :rtype : list
    :return:
    """
    return get_concept_stocks('GN036')

def stock_get_industry():
    """
    查询股票所属行业
    :param :security：标的代码，类型为字符串，形式如"000001.XSHE"；或为包含标的代码字符串的列表，形如["000001.XSHE", "000002.XSHE"]
            date：查询的日期。类型为字符串，形如"2018-06-01"或"2018-06-01 09:00:00"；或为datetime.datetime对象和datetime.date。注意传入对象的时分秒将被忽略
    :概念板块 : https://www.joinquant.com/data/dict/plateData#%E6%A6%82%E5%BF%B5%E6%9D%BF%E5%9D%97
    :rtype :dict
    :return:
    """
    return get_industry("600519.XSHG",date="2018-06-01")
