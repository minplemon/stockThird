#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-19 17:06
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : maketTong.py
# @Software: PyCharm

"""
##   市场通（沪港通、深港通和港股通）
###  AH股价格对比
     合格证券变动记录
     市场通交易日历
     市场通十大成交活跃股
     市场通成交与额度信息
     市场通汇率表
     沪深港通持股数据
     获取国际指数行情数据
参考 https://www.joinquant.com/help/api/help?name=JQData#%E5%B8%82%E5%9C%BA%E9%80%9A%EF%BC%88%E6%B2%AA%E6%B8%AF%E9%80%9A%E3%80%81%E6%B7%B1%E6%B8%AF%E9%80%9A%E5%92%8C%E6%B8%AF%E8%82%A1%E9%80%9A%EF%BC%89
"""
from jqdatasdk import *
auth('18620668927', 'minpeng123')   # 账号密码认证

def uu_query_STK_AH_PRICE_COMP():
    """
    记录同时在A股和H股上市的股票的价格比对
    :param :query(finance.STK_AH_PRICE_COMP)：表示从finance.STK_AH_PRICE_COMP这张表中查询同时在A股和H股上市的股票的价格对比，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：sqlalchemy.orm.query.Query对象
            finance.STK_AH_PRICE_COMP：代表A股和H股的价格对比表，收录了同时在A股和H股上市的股票的价格对比情况，包括收盘价，涨跌幅等，表结构和字段信息如下：
            字段	名称	类型	非空	备注/示例
            day	日期	date	Y
            name	股票简称	varchar(32)	Y
            a_code	a股代码	varchar(12)	Y	'000002.XSHE'
            h_code	h股代码	varchar(12)	Y
            a_price	a股收盘价	decimal(10,4)		人民币
            h_price	h股收盘价	decimal(10,4)		港币
            a_quote_change	a股涨跌幅	decimal(10,4)		%
            h_quote_change	h股涨跌幅	decimal(10,4)		%
            h_a_comp	比价(H/A)	decimal(10,4)		A股人民币价格/(H股港币价格*港币兑人民币的汇率)
            filter(finance.STK_AH_PRICE_COMP.a_code==a_code)：指定筛选条件，通过finance.STK_AH_PRICE_COMP.a_code==a_code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_AH_PRICE_COMP.day>='2015-01-01'，表示筛选日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。
            order_by(finance.STK_AH_PRICE_COMP.day): 将返回结果按日期排序
            limit(n)：限制返回的数据条数，n指定返回条数。
    :rtype :dataframe
    :return:
    """
    q = query(finance.STK_AH_PRICE_COMP).filter(finance.STK_AH_PRICE_COMP.a_code == '000002.XSHE').order_by(
        finance.STK_AH_PRICE_COMP.day).limit(10)
    df = finance.run_query(q)
    return df

def uu_query_STK_EL_CONST_CHANGE():
    """
    记录沪港通、深港通和港股通的成分股的变动情况
    :param :query(finance.STK_EL_CONST_CHANGE)：表示从finance.STK_EL_CONST_CHANGE这张表中查询沪港通、深港通和港股通成分股的变动记录，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_EL_CONST_CHANGE：代表合资格证券变动表，记录沪港通、深港通和港股通成分股的变动情况，包括交易类型，变更日期，变更方向等，表结构和字段信息如下：

            字段	名称	类型	非空	备注/示例
            link_id	交易类型编码	int	Y	同市场通编码
            link_name	交易类型名称	varchar(12)	Y
            code	证券代码	varchar(12)	Y
            name_ch	中文简称	varchar(30)
            name_en	英文简称	varchar(120)
            exchange	该股票所在的交易所	varchar(12)	Y	上海市场:XSHG/深圳市场:XSHE/香港市场:XHKG
            change_date	变更日期	date	Y
            direction	变更方向	varchar(6)	Y	IN/OUT（分别为纳入和剔除）
            filter(finance.STK_EL_CONST_CHANGE.code==code)：指定筛选条件，通过finance.STK_EL_CONST_CHANGE.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_EL_CONST_CHANGE.change_date>='2015-01-01'，表示筛选变更日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。
            order_by(finance.STK_EL_CONST_CHANGE.change_date): 将返回结果按变更日期排序
            limit(n):限制返回的数据条数，n指定返回条数。
    :rtype :dataframe
    :return:
    """
    q = query(finance.STK_EL_CONST_CHANGE).filter(finance.STK_EL_CONST_CHANGE.link_id == 310001).order_by(
        finance.STK_EL_CONST_CHANGE.change_date).limit(10)
    df = finance.run_query(q)
    return df

def uu_query_STK_EXCHANGE_LINK_CALENDAR():
    """
    记录沪港通、深港通和港股通每天是否开市
    :param :query(finance.STK_EXCHANGE_LINK_CALENDAR)：表示从finance.STK_EXCHANGE_LINK_CALENDAR这张表中查询市场沪港通、深港通和港股通交易日历的信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：sqlalchemy.orm.query.Query对象
            finance.STK_EXCHANGE_LINK_CALENDAR：代表市场通交易日历表，记录沪港通、深港通和港股通每天是否开市，包括交易日期，交易日类型等，表结构和字段信息如下：
            字段	名称	类型	非空	备注/示例
            day	交易日期	date	Y
            link_id	市场通编码	int	Y
            link_name	市场通名称	varchar(32)	Y	包括以下四个名称： 沪股通， 深股通， 港股通(沪)， 港股通(深)
            type_id	交易日类型编码	int	Y	如下 交易日类型编码
            type	交易日类型	varchar(32)	Y
            附注

            港股通（沪）和港股通（深）的交易日在深港通开展后是一致的。

            交易日类型编码

            交易日类型编码	交易日类型
            312001	正常交易日
            312002	周末
            312003	全天休市
            312004	上午休市
            312005	下午休市
            市场通编码

            市场通编码	市场通名称
            310001	沪股通
            310002	深股通
            310003	港股通（沪）
            310004	港股通（深）
            filter(finance.STK_EXCHANGE_LINK_CALENDAR.day==day)：指定筛选条件，通过finance.STK_EXCHANGE_LINK_CALENDAR.day==day可以指定你想要查询的日期；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_EXCHANGE_LINK_CALENDAR.type_id==312001，表示筛选交易日类型为正常交易日的数据；多个筛选条件用英文逗号分隔。
            limit(n)：限制返回的数据条数，n指定返回条数。
    :rtype :dataframe
    :return:
    """
    q = query(finance.STK_EXCHANGE_LINK_CALENDAR).filter(finance.STK_EXCHANGE_LINK_CALENDAR.day >= '2015-01-01').limit(
        10)
    df = finance.run_query(q)
    return df

def uu_query_STK_EL_TOP_ACTIVATE():
    """
    统计沪港通、深港通和港股通前十大交易活跃股的交易状况
    :param :query(finance.STK_EL_TOP_ACTIVATE)：表示从finance.STK_EL_TOP_ACTIVATE这张表中查询沪港通、深港通和港股通前十大交易活跃股的交易状况，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_EL_TOP_ACTIVATE：代表市场通十大成交活跃股数据表，统计沪港通、深港通和港股通前十大交易活跃股的交易状况，包括买入金额，卖出金额等，表结构和字段信息如下：

            字段	名称	类型	非空	交易所	备注/示例
            day	日期	date	Y
            link_id	市场通编码	int	Y
            link_name	市场通名称	varchar(32)	Y		包括以下四个名称： 沪股通， 深股通， 港股通(沪)， 港股通(深)
            rank	排名	int	Y
            code	股票代码	varchar(12)	Y
            name	股票名称	varchar(100)	Y
            exchange	交易所名称	varchar(12)	Y
            buy	买入金额(元)	decimal(20, 4)		Y
            sell	卖出金额(元)	decimal(20, 4)		Y
            total	买入及卖出金额(元)	decimal(20, 4)		Y
            市场通编码

            市场通编码	市场通名称
            310001	沪股通
            310002	深股通
            310003	港股通（沪）
            310004	港股通（深）
            filter(finance.STK_EL_TOP_ACTIVATE.code==code)：指定筛选条件，通过finance.STK_EL_TOP_ACTIVATE.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_EL_TOP_ACTIVATE.day>='2015-01-01'，表示筛选日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。
            limit(n)：限制返回的数据条数，n指定返回条数。
    :rtype :dataframe
    :return:
    """
    q = query(finance.STK_EL_TOP_ACTIVATE).filter(finance.STK_EL_TOP_ACTIVATE.code == '000002.XSHE').limit(10)
    df = finance.run_query(q)
    return df

def uu_query_STK_ML_QUOTA():
    """
    记录沪股通、深股通和港股通每个交易日的成交与额度的控制情况
    :param :query(finance.STK_ML_QUOTA)：表示从finance.STK_ML_QUOTA这张表中查询沪港通、深港通和港股通的成交与额度信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：sqlalchemy.orm.query.Query对象
            finance.STK_ML_QUOTA：代表了市场通成交与额度信息表，记录了沪港通、深港通和港股通成交与额度的信息，包括买入、卖出等，表结构和字段信息如下：
            字段	名称	类型	备注/示例
            day	交易日期	date
            link_id	市场通编码	int
            link_name	市场通名称	varchar(32)	包括以下四个名称： 沪股通，深股通，港股通(沪）,港股通(深）；其中沪股通和深股通属于北向资金，港股通（沪）和港股通（深）属于南向资金。
            currency_id	货币编码	int
            currency	货币名称	varchar(16)
            buy_amount	买入成交额	decimal(20,4)	亿
            buy_volume	买入成交数	decimal(20,4)	笔
            sell_amount	卖出成交额	decimal(20,4)	亿
            sell_volume	卖出成交数	decimal(20,4)	笔
            sum_amount	累计成交额	decimal(20,4)	买入成交额+卖出成交额
            sum_volume	累计成交数目	decimal(20,4)	买入成交量+卖出成交量
            quota	总额度	decimal(20, 4)	亿（2016-08-16号起，沪港通和深港通不再设总额度限制）
            quota_balance	总额度余额	decimal(20, 4)	亿
            quota_daily	每日额度	decimal(20, 4)	亿
            quota_daily_balance	每日额度余额	decimal(20, 4)	亿
            货币编码

            货币编码	货币名称
            110001	人民币
            110003	港元
            市场通编码

            市场通编码	市场通名称
            310001	沪股通
            310002	深股通
            310003	港股通（沪）
            310004	港股通（深）
            filter(finance.STK_ML_QUOTA.day==day)：指定筛选条件，通过finance.STK_ML_QUOTA.day==day可以指定你想要查询的日期；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_ML_QUOTA.link_id==310001，表示筛选市场通编码为310001（沪股通）的数据；多个筛选条件用英文逗号分隔。
            limit(n)：限制返回的数据条数，n指定返回条数
    :rtype :dataframe
    :return:
    """
    q = query(finance.STK_ML_QUOTA).filter(finance.STK_ML_QUOTA.day >= '2015-01-01').limit(10)
    df = finance.run_query(q)
    return df

def uu_query_STK_EXCHANGE_LINK_RATE():
    """
    包含2014年11月起人民币和港币之间的参考汇率/结算汇兑比率信息
    :param :query(finance.STK_EXCHANGE_LINK_RATE)：表示从finance.STK_EXCHANGE_LINK_RATE这张表中查询汇率信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_EXCHANGE_LINK_RATE：代表市场通汇率表，记录参考汇率/结算汇兑比率信息，包括买入参考/结算汇率、卖出参考/结算汇率等，表结构和字段信息如下：

            字段	名称	类型	非空	交易所	备注/示例
            day	日期	Date	Y	Y
            link_id	市场通编码	int	Y
            link_name	市场通名称	varchar(32)	Y		以“港股通(沪)”为代表
            domestic_currency	本币	varchar(12)	Y		RMB
            foreign_currency	外币	varchar(12)	Y		HKD
            refer_bid_rate	买入参考汇率	decimal(10, 5)	Y	Y
            refer_ask_rate	卖出参考汇率	decimal(10, 5)	Y	Y
            settle_bid_rate	买入结算汇率	decimal(10, 5)	Y	Y
            settle_ask_rate	卖出结算汇率	decimal(10, 5)	Y	Y
            市场通编码

            市场通编码	市场通名称
            310001	沪股通
            310002	深股通
            310003	港股通（沪）
            310004	港股通（深）
            filter(finance.STK_EXCHANGE_LINK_RATE.day==day)：指定筛选条件，通过finance.STK_EXCHANGE_LINK_RATE.day==day可以指定你想要查询的日期；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_EXCHANGE_LINK_RATE.link_id==310001，表示筛选市场通编码为310001（沪股通）的数据；多个筛选条件用英文逗号分隔。
            limit(n)：限制返回的数据条数，n指定返回条数。
    :rtype :dataframe
    :return:
    """
    q = query(finance.STK_EXCHANGE_LINK_RATE).filter(finance.STK_EXCHANGE_LINK_RATE.day >= '2015-01-01').limit(10)
    df = finance.run_query(q)
    return df

def uu_query_STK_HK_HOLD_INFO():
    """
    记录了北向资金（沪股通、深股通）和南向资金港股通的持股数量和持股比例
    :param :query(finance.STK_HK_HOLD_INFO)：表示从finance.STK_HK_HOLD_INFO这张表中查询沪深港通的持股数据，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号分隔进行提取；如query(finance.STK_HK_HOLD_INFO.code)。query函数的更多用法详见：query简易教程。
            finance.STK_HK_HOLD_INFO：收录了沪深港通每日的持股数量和持股比例数据，表结构和字段信息如下：
            字段名称	中文名称	字段类型	能否为空	注释
            day	日期	date	N
            link_id	市场通编码	int	N	三种类型：310001-沪股通，310002-深股通，310005-港股通
            link_name	市场通名称	varchar(32)	N	三种类型：沪股通，深股通，港股通
            code	股票代码	varchar(12)	N
            name	股票名称	varchar(100)	N
            share_number	持股数量	int		单位：股，于中央结算系统的持股量
            share_ratio	持股比例	decimal(10,4)		单位：％，沪股通：占于上交所上市及交易的A股总数的百分比；深股通：占于深交所上市及交易的A股总数的百分比；港股通：占已发行股份百分比
            filter(finance.STK_HK_HOLD_INFO.link_id==310001)：指定筛选条件，通过finance.STK_HK_HOLD_INFO.link_id==310001可以指定查询沪股通的持股数据；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_HK_HOLD_INFO.day=='2019-03-01'，指定获取2019年3月1日的沪深港通持股数据。
            limit(n)：限制返回的数据条数，n指定返回条数。
    :rtype :dataframe
    :return:
    """
    df = finance.run_query(query(finance.STK_HK_HOLD_INFO).filter(finance.STK_HK_HOLD_INFO.link_id == 310001).order_by(
        finance.STK_HK_HOLD_INFO.day.desc()))
    return df

def uu_query_GLOBAL_IDX_DAILY():
    """
    获取港美股指数日行情数据
    :param :query(finance.GLOBAL_IDX_DAILY)：表示从finance.GLOBAL_IDX_DAILY这张表中查询港美股指数日行情的数据，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：sqlalchemy.orm.query.Query对象
            finance.GLOBAL_IDX_DAILY：收录了港美股各个指数数据，表结构和字段信息如下：
            字段设计

            字段	名称	类型	释义
            code	指数代码	varchar(64)	800000.XHKG-恒生指数；800100.XHKG-国企指数；800151.XHKG-红筹指数；INX-标普500指数；IXIC-纳斯达克综合指数；DJI-道琼斯指数
            name	指数名称	varchar(64)
            day	日期	date
            open	开盘价	decimal(20,6)
            close	收盘价	decimal(20,6)
            low	最低价	decimal(20,6)
            high	最高价	decimal(20,6)
            volume	成交量	decimal(20,6)
            change_pct	涨跌幅	decimal(20,4)
            pre_close	前收价	decimal(20,6)
            filter(finance.GLOBAL_IDX_DAILY.code==code)：指定筛选条件，通过finance.GLOBAL_IDX_DAILY.code==code可以指定您想要查询的指数代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.GLOBAL_IDX_DAILY.day.desc()，表示按天倒序排名。
            limit(n)：限制返回的数据条数，n指定返回条数。
    :rtype :dataframe
    :return:
    """
    # 查询美股指数标普500('INX')近十天的指数数据
    q = query(finance.GLOBAL_IDX_DAILY).filter(finance.GLOBAL_IDX_DAILY.code == 'INX').order_by(
        finance.GLOBAL_IDX_DAILY.day.desc()).limit(10)
    df = finance.run_query(q)
    return df

q=query(finance.GLOBAL_IDX_DAILY).filter(finance.GLOBAL_IDX_DAILY.code=='INX').order_by(finance.GLOBAL_IDX_DAILY.day.desc()).limit(10)
df=finance.run_query(q)
print(df)