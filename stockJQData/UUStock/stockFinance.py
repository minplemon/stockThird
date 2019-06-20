#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-20 10:06
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : stockFinance.py
# @Software: PyCharm

"""
##   获取单季度/年度财务数据
###  查询股票的市值数据、资产负债数据、现金流数据、利润数据、财务指标数据
参考  https://www.joinquant.com/help/api/help?name=Stock#%E8%8E%B7%E5%8F%96%E5%8D%95%E5%AD%A3%E5%BA%A6%E5%B9%B4%E5%BA%A6%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE
"""
from jqdatasdk import *
auth('18620668927', 'minpeng123')   # 账号密码认证 可通过注册 聚宽领取 https://www.joinquant.com

def uu_get_fundamentals():
    """
    :表名 : valuation 市值数据
            balance 资产负债数据
            cash_flow 现金流数据
            income 利润数据
            indicator 财务指标数据
            bank_indicator 银行业专项指标
            security_indicator 券商业专项指标
            insurance_indicator 保险业专项指标
    :param :query_object: 一个sqlalchemy.orm.query.Query对象, 可以通过全局的query函数获取Query对象，query简易教程。
            date: 查询日期, 一个字符串(格式类似’2015-10-15’)或者[datetime.date]/[datetime.datetime]对象, 可以是None, 使用默认日期. 这个默认日期在回测和研究模块上有点差别:
    :return:
    """

    # 查询'000001.XSHE'的所有市值数据, 时间是2015-10-15
    q = query(
        valuation
    ).filter(
        valuation.code == '000001.XSHE'
    )
    df = get_fundamentals(q, '2015-10-15')
    # 打印出总市值
    log.info(df['market_cap'][0])
    return df