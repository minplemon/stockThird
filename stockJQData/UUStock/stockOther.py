#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-20 10:12
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : stockOther.py
# @Software: PyCharm

"""
##   股票数据
###  融资融券信息 平台可交易的成分股列表 行业分类列表 概念分类列
参考  https://www.joinquant.com/help/api/help?name=Stock#%E8%8E%B7%E5%8F%96%E8%82%A1%E7%A5%A8%E6%95%B0%E6%8D%AE
"""
from jqdatasdk import *
auth('18620668927', 'minpeng123')   # 账号密码认证 可通过注册 聚宽领取 https://www.joinquant.com

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