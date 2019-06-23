#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-14 16:57
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : jqdata.py
# @Software: PyCharm

from jqdatasdk import *
from jqdatasdk.alpha101 import *
from jqdatasdk import alpha191
from jqdatasdk.technical_analysis import *
auth('18620668927', 'minpeng123')
#查询当日剩余可调用数据条数
# count=get_query_count()
# print(count)
security_list1 = '000004.XSHE'
# security_list2 = ['000001.XSHE','000002.XSHE','601211.XSHG','603177.XSHG']
# 计算并输出 security_list1 的 KDJ 值
K1,D1,J1 = KDJ(security_list1, check_date='2019-05-13', N =9, M1=3, M2=3)
print(K1[security_list1])
print (D1[security_list1])
print (J1[security_list1])
print('-------')
#
# # 输出 security_list2 的 KDJ 值
# K2,D2,J2 = KDJ(security_list2, check_date='2017-01-04', N =9, M1=3, M2=3)
# for stock in security_list2:
#     print (K2[stock])
#     print (D2[stock])
#     print (J2[stock])


# security_list1 = '000001.XSHE'
# security_list2 = ['000001.XSHE','000002.XSHE','601211.XSHG','603177.XSHG']
#
# # 计算并输出 security_list1 的 ACCER 值
# ACCER1 = ACCER(security_list1, check_date='2017-01-04', N = 8)
# print (ACCER1[security_list1])
#
# # 输出 security_list2 的 ACCER 值
# ACCER2 = ACCER(security_list2, check_date='2017-01-04', N = 8)
# for stock in security_list2:
#     print (ACCER2[stock])

## 各种榜
sdfd = get_billboard_list(stock_list=None, end_date = '2019-05-13', count =1)
print(sdfd)

