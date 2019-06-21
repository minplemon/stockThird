#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-20 18:00
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : fundOn.py
# @Software: PyCharm

"""
##   获取场内基金份额数据
###  获取场内基金份额数据
参考  https://www.joinquant.com/help/api/help?name=JQData#%E8%8E%B7%E5%8F%96%E5%9C%BA%E5%86%85%E5%9F%BA%E9%87%91%E4%BB%BD%E9%A2%9D%E6%95%B0%E6%8D%AE
"""
from jqdatasdk import *
auth('18620668927', 'minpeng123')   # 账号密码认证

def stock_query_FUND_SHARE_DAILY():
    """
    获取场内基金份额数据
    描述：记录每日场内基金份额数据
    :param :query(finance.FUND_SHARE_DAILY)：表示从finance.FUND_SHARE_DAILY这张表中查询每日场内基金份额数据，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：query简易教程
            finance.FUND_SHARE_DAILY：收录了每日场内基金份额数据，表结构和字段信息如下：
            字段设计：

            名称	类型	描述
            code	varchar(12)	基金代码
            name	varchar(50）	基金简称
            exchange_code	varchar(12)	交易市场编码，XSHG-上海证券交易所；XSHE-深圳证券交易所
            date	date	日期
            shares	bigint	基金份额（份）
            filter(finance.FUND_SHARE_DAILY.date==date)：指定筛选条件，通过finance.FUND_SHARE_DAILY.date==date可以指定你想要查询的日期；除此之外，还可以对表中其他字段指定筛选条件；多个筛选条件用英文逗号分隔。
            limit(n)：限制返回的数据条数，n指定返回条数。
    :rtype :dataframe
    :return:
    """
    # 查询2019-05-23的场内基金份额数据
    df = finance.run_query(
        query(finance.FUND_SHARE_DAILY).filter(finance.FUND_SHARE_DAILY.date == '2019-05-23').limit(10))
    return df


#查询2019-05-23的场内基金份额数据
df=finance.run_query(query(finance.FUND_SHARE_DAILY).filter(finance.FUND_SHARE_DAILY.date=='2019-05-23').limit(10))

print(df)