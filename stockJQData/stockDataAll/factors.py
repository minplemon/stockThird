#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-22 10:45
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : factors.py
# @Software: PyCharm

"""
##   聚宽因子库（付费）
###  获取因子值
     获取所有因子
     单因子分层回测函数
     因子列表
参考 https://www.joinquant.com/help/api/help?name=JQData#%E8%81%9A%E5%AE%BD%E5%9B%A0%E5%AD%90%E5%BA%93%EF%BC%88%E4%BB%98%E8%B4%B9%EF%BC%89
"""

from jqdatasdk import *
import logging as log
import pandas as pd
import os
auth('18620668927', 'minpeng123')   # 账号密码认证
path = os.getcwd()

def stock_get_factor_values(stock,start_date,end_date):
    """
    获取因子值
    :param :securities:股票池，单只股票（字符串）或一个股票列表
            factors: 因子名称，单个因子（字符串）或一个因子列表
            start_date:开始日期，字符串或 datetime 对象，与 coun t参数二选一
            end_date: 结束日期， 字符串或 datetime 对象，可以与 start_date 或 count 配合使用
            count: 截止 end_date 之前交易日的数量（含 end_date 当日），与 start_date 参数二选一
                :rtype :一个 dict： key 是因子名称， value 是 pandas.dataframe
    :return:
    """
    # 获取因子Skewness60(个股收益的60日偏度)从 2017-01-01 至 2017-03-04 的因子值
    factor_data = get_factor_values(securities=[stock], factors=[
                    'eps_ttm','net_asset_per_share','capital_reserve_fund_per_share','retained_profit_per_share',
                    'net_operate_cash_flow_per_share'],
                                    start_date=start_date, end_date=end_date)
    # 查看因子值
    # eps_ttm = factor_data['eps_ttm'] # 每股收益TTM
    # net_asset_per_share = factor_data['net_asset_per_share'] # 每股净资产
    # capital_reserve_fund_per_share = factor_data['capital_reserve_fund_per_share'] # 每股资本公积金
    # retained_profit_per_share = factor_data['retained_profit_per_share'] # 每股未分配利润
    # net_operate_cash_flow_per_share = factor_data['net_operate_cash_flow_per_share'] # 每股经营活动产生的现金流量净额
    # df = pd.merge(eps_ttm,net_asset_per_share,how='left')
    return factor_data

def stock_get_all_factors():
    """
    获取所有因子
    :rtype :pandas.DataFrame
    :return:factor:因子code
            factor_intro:因子说明
            category:因子分类名称
            category_intro:因子分类说明
    """
    df = get_all_factors()
    return df
# filename = path + '/bigfile.csv'
#
# df = uu_get_all_factors()
# df.to_csv(filename)
# print(df)

# #获取聚宽因子库营业收入TTM因子“operating_revenue_ttm”的分层回测收益
# df =get_factor_effect('000001.XSHE','2019-01-01','2019-03-30','1M','operating_revenue_ttm',5)
# print(df)

# df = uu_get_factor_values()
# print(df)