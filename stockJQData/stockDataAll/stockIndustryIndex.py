#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-20 11:34
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : stockIndustryIndex.py
# @Software: PyCharm

"""
##   获取行业指数数据
###  获取申万一级行业日行情数据
     获取申万一级行业估值数据
参考：https://www.joinquant.com/help/api/help?name=JQData#%E8%8E%B7%E5%8F%96%E8%A1%8C%E4%B8%9A%E6%8C%87%E6%95%B0%E6%95%B0%E6%8D%AE
"""
from jqdatasdk import *
auth('18620668927', 'minpeng123')   # 账号密码认证 可通过注册 聚宽领取 https://www.joinquant.com

def stock_query_SW1_DAILY_PRICE():
    """
    获取申万一级行业日行情数据
    记录了申万一级行业指数的历史日行情数据，每日18:00更新
    :param :query(finance.SW1_DAILY_PRICE)：表示从finance.SW1_DAILY_PRICE这张表中查询申万一级行业指数的历史日行情数据，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号分隔进行提取；如query(finance.SW1_DAILY_PRICE.code)。query函数的更多用法详见：query简易教程。
            finance.SW1_DAILY_PRICE：代表申万一级行业日行情数据表，收录了申万一级行业指数的历史日行情数据，表结构和字段信息如下：
            字段名称	中文名称	字段类型	能否为空	注释
            date	交易日	date	N
            code	指数编码	varchar(12)	N	对应申万一级行业指数编码
            name	指数名称	varchar(20)	N
            open	开盘指数	decimal(20,4)
            high	最高指数	decimal(20,4)
            low	最低指数	decimal(20,4)
            close	收盘指数	decimal(20,4)
            pre_close	昨收盘指数	decimal(20,4)		昨收盘指数用昨日的收盘指数填充
            volume	成交量	decimal(20,4)		单位：股
            money	成交额	decimal(20,4)		单位：元
            change_pct	涨跌幅	decimal(10,4)		单位：％
            filter(finance.SW1_DAILY_PRICE.code==801010)：指定筛选条件，通过finance.SW1_DAILY_PRICE.code==801010可以查询指定行业（如农林牧渔801010）的日行情数据；除此之外，还可以对表中其他字段指定筛选条件，如finance.SW1_DAILY_PRICE.date=='2019-03-01'，指定获取2019年3月1日的申万一级行业日行情数据。
            limit(n)：限制返回的数据条数，n指定返回条数。
    :rtype :dataframe
    :return:
    """

    # 查询最近10个交易日申万一级行业指数-农林牧渔行业（801010）的日行情数据。
    return finance.run_query(query(finance.SW1_DAILY_PRICE).filter(finance.SW1_DAILY_PRICE.code=='801010').order_by(finance.SW1_DAILY_PRICE.date.desc()).limit(10))

def stock_query_SW1_DAILY_VALUATION():
    """
    :param :query(finance.SW1_DAILY_VALUATION)：表示从finance.SW1_DAILY_VALUATION这张表中查询申万一级行业指数的估值数据，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号分隔进行提取；如query(finance.SW1_DAILY_VALUATION.code)。query函数的更多用法详见：query简易教程。
            finance.SW1_DAILY_VALUATION：代表申万一级行业指数估值表，收录了申万一级行业指数的历史估值数据，表结构和字段信息如下：
            字段名称	中文名称	字段类型	能否为空	注释
            date	交易日	date	N
            code	指数编码	varchar(12)	N	对应申万一级行业指数编码
            name	指数名称	varchar(20)	N
            turnover_ratio	换手率	decimal(10,4)		单位：％
            pe	市盈率	decimal(20,4)		单位：倍；PE = 流通市值／最近4个季度的净利润；最近 4 个季度的净利润按如下方法计算: 1-4 月,最近 4 个季度的净利润=上一年度前 3 季度累计净利润+上上一年度的四季度净利润；5-8 月,最近 4 个季度的净利润=当年 1 季度净利润+前 1 年净利润-前 1 年 1 季度净利润；9-10 月,最近 4 个季度的净利润=当年中期净利润+前 1 年净利润-前 1 年中期净利润；11-12 月,最近 4 个季度的净利润=当年前 3 季度累计净利润+上1年年度净利润-上 1 年前 3 季度累计净利润
            pb	市净率	decimal(20,4)		单位：倍；按照自由流通量加权的净资产倍率。 PB = 流通市值／按照流通市值计算的净资产；按照流通市值计算的净资产 ＝ 最新净资产*流通股本／总股本
            average_price	均价	decimal(20,4)		单位：元。指数成份股在统计期最后交易日收盘的简单算术平均价
            money_ratio	成交额占比	decimal(10,4)		单位：％；成交额占比＝某个行业成交额／所有行业成交额之和
            circulating_market_cap	流通市值	decimal(20,4)		单位：元
            average_circulating_market_cap	平均流通市值	decimal(20,4)		单位：元；平均流通市值＝流通市值／所在行业股票数
            dividend_ratio	股息率	decimal(10,4)		单位：％；按照自由流通量加权的现金股息率；dividend_ratio=Df/Vf；Df: 所有股票在截止日的一 个自然年(365日)中所累积派发的税前现金红利之和按照流通股本对应的分红量；Vf: 该行业成分股股的流通市值之和
            filter(finance.SW1_DAILY_VALUATION.code==801010)：指定筛选条件，通过finance.SW1_DAILY_VALUATION.code=='801010'可以查询指定行业（如农林牧渔801010）的估值数据；除此之外，还可以对表中其他字段指定筛选条件，如finance.SW1_DAILY_VALUATION.date=='2019-03-01'，指定获取2019年3月1日的申万一级行业的估值数据。
            limit(n)：限制返回的数据条数，n指定返回条数。
    :rtype :dataframe
    :return:
    """

    # 查询最近10个交易日申万一级行业指数-农林牧渔行业（801010）的估值数据
    return finance.run_query(query(finance.SW1_DAILY_VALUATION).filter(finance.SW1_DAILY_VALUATION.code=='801010').limit(n))


df=finance.run_query(query(finance.SW1_DAILY_VALUATION).filter(finance.SW1_DAILY_VALUATION.code=='801010').order_by(finance.SW1_DAILY_VALUATION.date.desc()).limit(10))
print(df)