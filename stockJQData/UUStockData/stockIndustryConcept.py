#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-20 11:11
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : stockIndustryConcept.py
# @Software: PyCharm

"""
##   获取行业概念成分股
###  get_industries - 获取行业列表
     get_industry_stocks - 获取行业成份股
     get_concepts - 获取概念列表
     get_concept_stocks - 获取概念成份股
     get_industry - 查询股票所属行业
参考  https://www.joinquant.com/help/api/help?name=JQData#%E8%8E%B7%E5%8F%96%E8%A1%8C%E4%B8%9A%E6%A6%82%E5%BF%B5%E6%88%90%E5%88%86%E8%82%A1
"""
from jqdatasdk import *
auth('18620668927', 'minpeng123')   # 账号密码认证 可通过注册 聚宽领取 https://www.joinquant.com


def uu_get_industries():
    """
    按照行业分类获取行业列表
    :param :name: 行业代码， 取值如下：
            "sw_l1": 申万一级行业
            "sw_l2": 申万二级行业
            "sw_l3": 申万三级行业
            "jq_l1": 聚宽一级行业
            "jq_l2": 聚宽二级行业
            "zjw": 证监会行业
    :rtype :pandas.DataFrame
    :return:index: 行业代码
            name: 行业名称
            start_date: 开始日期
    """
    return get_industries(name='zjw')

def uu_get_industry_stocks():
    """
    获取在给定日期一个行业的所有股票
    :行业列表 : https://www.joinquant.com/help/api/help?name=plateData
    :param :industry_code: 行业编码
            date: 查询日期, 一个字符串(格式类似'2015-10-15')或者[datetime.date]/[datetime.datetime]对象, 可以是None.
    :rtype :list
    :return:
    """
    # 获取计算机/互联网行业的成分股
    return get_industry_stocks('I64')
def uu_get_concepts():
    """
    获取概念板块列表
    :param :
    :rtype :pandas.DataFrame
    :return:index: 概念代码
            name: 概念名称
            start_date: 开始日期
    """
    return get_concepts()
def uu_get_concept_stocks():
    """
    获取在给定日期一个概念板块的所有股票
    行业概念数据 :https://www.joinquant.com/data/dict/plateData
    :param :concept_code: 概念板块编码
            date: 查询日期, 一个字符串(格式类似'2015-10-15')或者[datetime.date]/[datetime.datetime]对象, 可以是None.
    :rtype :list
    :return:
    """
    # 获取风力发电概念板块的成分股
    return get_concept_stocks('GN036')
def uu_get_industry(stock,date):
    """
    查询股票所属行业
    :param :security：标的代码，类型为字符串，形式如"000001.XSHE"；或为包含标的代码字符串的列表，形如["000001.XSHE", "000002.XSHE"]
            date：查询的日期。类型为字符串，形如"2018-06-01"或"2018-06-01 09:00:00"；或为datetime.datetime对象和datetime.date。注意传入对象的时分秒将被忽略。
    :rtype :dict
    :return:
    """
    return get_industry(stock,date=date)


# df = uu_get_industry_stocks()
# print(df)