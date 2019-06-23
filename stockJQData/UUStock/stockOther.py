#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-19 15:16
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : stockOther.py
# @Software: PyCharm

# 获取行情数据
"""
##   股票数据
###  上市公司分红送股（除权除息）数据
     沪深市场每日成交概况
     获取融资融券汇总数据
参考  https://www.joinquant.com/help/api/help?name=JQData#%E4%B8%8A%E5%B8%82%E5%85%AC%E5%8F%B8%E5%88%86%E7%BA%A2%E9%80%81%E8%82%A1%EF%BC%88%E9%99%A4%E6%9D%83%E9%99%A4%E6%81%AF%EF%BC%89%E6%95%B0%E6%8D%AE
"""
from jqdatasdk import *
auth('18620668927', 'minpeng123')   # 账号密码认证

def uu_query_STK_XR_XD():
    """
    记录由上市公司年报、中报、一季报、三季报统计出的分红转增情况
    :param :query(finance.STK_XR_XD)：表示从finance.STK_XR_XD这张表中查询上市公司除权除息的数据，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_XR_XD：代表除权除息数据表，记录由上市公司年报、中报、一季报、三季报统计出的分红转增情况。表结构和字段信息如下：

            字段名称	中文名称	字段类型	能否为空	含义
            code	股票代码	varchar(12)	N	加后缀
            company_id	机构ID	int	N
            company_name	机构名称	varchar(100)
            report_date	分红报告期	date	N	一般为：一季报:YYYY-03-31;中报:YYYY-06-30;三季报:YYYY-09-30;年报:YYYY-12-31同时也可能存在其他日期
            bonus_type	分红类型	varchar(60)		201102新增,类型如下：年度分红 中期分红 季度分红 特别分红 向公众股东赠送 股改分红
            board_plan_pub_date	董事会预案公告日期	date
            board_plan_bonusnote	董事会预案分红说明	varchar(500)		每10股送XX转增XX派XX元
            distributed_share_base_board	分配股本基数（董事会）	decimal(20,4)		单位:万股
            shareholders_plan_pub_date	股东大会预案公告日期	date
            shareholders_plan_bonusnote	股东大会预案分红说明	varchar(200)
            distributed_share_base_shareholders	分配股本基数（股东大会）	decimal(20,4)		单位:万股
            implementation_pub_date	实施方案公告日期	date
            implementation_bonusnote	实施方案分红说明	varchar(200)		维护规则: 每10股送XX转增XX派XX元 或:不分配不转赠
            distributed_share_base_implement	分配股本基数（实施）			单位:万股
            dividend_ratio	送股比例	decimal(20,4)		每10股送XX股
            transfer_ratio	转增比例	decimal(20,4)		每10股转增 XX股 ；
            bonus_ratio_rmb	派息比例(人民币)	decimal(20,4)		每10股派 XX。说明：这里的比例为最新的分配比例，预案公布的时候，预案的分配基数在此维护，如果股东大会或实施方案发生变化，再次进行修改，保证此处为最新的分配基数
            bonus_ratio_usd	派息比例（美元）	decimal(20,4)		每10股派 XX。说明：这里的比例为最新的分配比例，预案公布的时候，预案的分配基数在此维护，如果股东大会或实施方案发生变化，再次进行修改，保证此处为最新的分配基数 如果这里只告诉了汇率，没有公布具体的外币派息，则要计算出；
            bonus_ratio_hkd	派息比例（港币）	decimal(20,4)		每10股派 XX。说明：这里的比例为最新的分配比例，预案公布的时候，预案的分配基数在此维护，如果股东大会或实施方案发生变化，再次进行修改，保证此处为最新的分配基数 如果这里只告诉了汇率，没有公布具体的外币派息，则要计算出；
            at_bonus_ratio_rmb	税后派息比例（人民币）	decimal(20,4)
            exchange_rate	汇率	decimal(20,4)		当日以外币（美元或港币）计价的B股价格兑换成人民币的汇率
            dividend_number	送股数量	decimal(20,4)		单位：万股
            transfer_number	转增数量	decimal(20,4)		单位：万股
            bonus_amount_rmb	派息金额(人民币)	decimal(20,4)		单位：万元
            a_registration_date	A股股权登记日	date
            b_registration_date	B股股权登记日	date		B股股权登记存在最后交易日，除权基准日以及股权登记日三个日期，由于B股实行T+3制度，最后交易日持有的股份需要在3个交易日之后确定股东身份，然后在除权基准日进行除权。
            a_xr_date	A股除权日	date
            b_xr_baseday	B股除权基准日	date		根据B股实行T＋3交收制度,则B股的“股权登记日”是“最后交易日”后的第 三个交易日,直至“股权登记日”这一日为止,B股投资者的股权登记才告完成,也 就意味着B股股份至股权登记日为止,才真正划入B股投资者的名下。
            b_final_trade_date	B股最后交易日	date
            a_bonus_date	派息日(A)	date
            b_bonus_date	派息日(B)	date
            dividend_arrival_date	红股到帐日	date
            a_increment_listing_date	A股新增股份上市日	date
            b_increment_listing_date	B股新增股份上市日	date
            total_capital_before_transfer	送转前总股本	decimal(20,4)		单位：万股
            total_capital_after_transfer	送转后总股本	decimal(20,4)		单位：万股
            float_capital_before_transfer	送转前流通股本	decimal(20,4)		单位：万股
            float_capital_after_transfer	送转后流通股本	decimal(20,4)		单位：万股
            note	备注	varchar(500)
            a_transfer_arrival_date	A股转增股份到帐日	date
            b_transfer_arrival_date	B股转增股份到帐日	date
            b_dividend_arrival_date	B股送红股到帐日	date		20080801新增
            note_of_no_dividend	有关不分配的说明	varchar(1000)
            plan_progress_code	方案进度编码	int
            plan_progress	方案进度	varchar(60)		董事会预案 实施方案 股东大会预案 取消分红 公司预案
            bonus_cancel_pub_date	取消分红公告日期	date
            filter(finance.STK_XR_XD.report_date==report_date)：指定筛选条件，通过finance.STK_XR_XD.report_date==report_date可以指定你想要查询的分红报告期；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_XR_XD.code=='000001.XSHE'，表示筛选股票编码为000001.XSHE的数据； 多个筛选条件用英文逗号分隔。

            order_by(finance.STK_XR_XD.report_date): 将返回结果按分红报告期排序

            limit(n)：限制返回的数据条数，n指定返回条数
    :rtype :dataframe
    :return:
    """
    q = query(finance.STK_XR_XD).filter(finance.STK_XR_XD.report_date >= '2015-01-01').limit(10)
    df = finance.run_query(q)
    return df


def uu_query_STK_EXCHANGE_TRADE_INFO():
    """
    记录沪深两市股票交易的成交情况，包括市值、成交量，市盈率等情况
    :param :query(finance.STK_EXCHANGE_TRADE_INFO)：表示从finance.STK_EXCHANGE_TRADE_INFO这张表中查询沪深两市股票交易的成交情况，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：query简易教程
            finance.STK_EXCHANGE_TRADE_INFO：代表沪深市场每日成交概况表，记录沪深两市股票交易的成交情况，包括市值、成交量，市盈率等情况，表结构和字段信息如下：
            字段名称	中文名称	字段类型	能否为空	含义
            exchange_code	市场编码	varchar(12)	N	编码规则见下表
            exchange_name	市场名称	varchar(100)		上海市场，上海A股，上海B股，深圳市场，深市主板，中小企业板，创业板
            date	交易日期	date	N
            total_market_cap	市价总值	decimal(20,8)		单位：亿
            circulating_market_cap	流通市值	decimal(20,8)		单位：亿
            volume	成交量	decimal(20,4)		单位：万
            money	成交金额	decimal(20,8)		单位：亿
            deal_number	成交笔数	decimal(20,4)		单位：万笔
            pe_average	平均市盈率	decimal(20,4)		上海市场市盈率计算方法：市盈率＝∑(收盘价×发行数量)/∑(每股收益×发行数量)，统计时剔除亏损及暂停上市的上市公司。深圳市场市盈率计算方法：市盈率＝∑市价总值/∑(总股本×上年每股利润)，剔除上年利润为负的公司。
            turnover_ratio	换手率	decimal(10,4)		单位：％
            市场编码名称对照表

            市场编码	交易市场名称	备注
            322001	上海市场
            322002	上海A股
            322003	上海B股
            322004	深圳市场	该市场交易所未公布成交量和成交笔数
            322005	深市主板
            322006	中小企业板
            322007	创业板
            filter(finance.STK_EXCHANGE_TRADE_INFO.date==date)：指定筛选条件，通过finance.STK_EXCHANGE_TRADE_INFO.date==date可以指定你想要查询的交易日期；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_EXCHANGE_TRADE_INFO.exchange_code==322001，表示筛选市场编码为322001（上海市场）的数据；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数。
    :rtype :dataframe
    :return:
    """
    q = query(finance.STK_EXCHANGE_TRADE_INFO).filter(finance.STK_EXCHANGE_TRADE_INFO.date >= '2015-01-01').limit(10)
    df = finance.run_query(q)
    return df


def uu_query_STK_MT_TOTAL():
    """
    描述：记录上海交易所和深圳交易所的融资融券汇总数据
    :param :query(finance.STK_MT_TOTAL)：表示从finance.STK_MT_TOTAL这张表中查询融资融券汇总数据，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：query简易教程
            finance.STK_MT_TOTAL：收录了融资融券汇总数据，表结构和字段信息如下：
            字段设计

            名称	类型	描述
            date	date	交易日期
            exchange_code	varchar(12)	交易市场。例如，XSHG-上海证券交易所；XSHE-深圳证券交易所。对应DataAPI.SysCodeGet.codeTypeID=10002。
            fin_value	decimal(20,2)	融资余额（元）
            fin_buy_value	decimal(20,2)	融资买入额（元）
            sec_volume	int	融券余量（股）
            sec_value	decimal(20,2)	融券余量金额（元）
            sec_sell_volume	int
    :rtype :dataframe
    :return:
    """
    df = finance.run_query(query(finance.STK_MT_TOTAL).filter(finance.STK_MT_TOTAL.date == '2019-05-23').limit(10))
    return df


df=finance.run_query(query(finance.STK_MT_TOTAL).filter(finance.STK_MT_TOTAL.date=='2019-05-23').limit(10))
print(df)