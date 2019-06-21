#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-19 17:08
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : financeDateData.py
# @Software: PyCharm

# 查询股票的市值数据、资产负债数据、现金流数据、利润数据、财务指标数据. 详情通过财务数据列表查看!
"""
##   获取单季度/年度财务数据
###  get_fundamentals - 查询财务数据
     get_fundamentals_continuously - 查询多日的财务数据
     市值数据（每日更新）
     财务指标数据
参考  https://www.joinquant.com/help/api/help?name=JQData#%E8%8E%B7%E5%8F%96%E5%8D%95%E5%AD%A3%E5%BA%A6%E5%B9%B4%E5%BA%A6%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE
"""
from jqdatasdk import *
import logging as log
auth('18620668927', 'minpeng123')   # 账号密码认证

def stock_get_fundamentals():
    """
    查询财务数据
    :财务数据文档 :https://www.joinquant.com/help/api/help?name=Stock#%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE%E5%88%97%E8%A1%A8
    :表名 : valuation 市值数据
            balance 资产负债数据
            cash_flow 现金流数据
            income 利润数据
            indicator 财务指标数据
            bank_indicator 银行业专项指标
            security_indicator 券商业专项指标
            insurance_indicator 保险业专项指标
    :param :query_object: 一个sqlalchemy.orm.query.Query对象，可以通过全局的 query 函数获取 Query 对象，query简易教程

            date: 查询日期, 一个字符串(格式类似'2015-10-15')或者[datetime.date]/[datetime.datetime]对象, 可以是None, 使用默认日期. 如果传入的 date 不是交易日, 则使用这个日期之前的最近的一个交易日

            statDate: 财报统计的季度或者年份, 一个字符串, 有两种格式:
    :rtype :pandas.DataFrame
    :return:
    :其他实例
            # 查询'000001.XSHE'的所有市值数据, 时间是2015-10-15
            q = query(
                valuation
            ).filter(
                valuation.code == '000001.XSHE'
            )
            df = get_fundamentals(q, '2015-10-15')
            # 打印出总市值
            print(df['market_cap'][0])
            # 获取多只股票在某一日期的市值, 利润
            df = get_fundamentals(query(
                    valuation, income
                ).filter(
                    # 这里不能使用 in 操作, 要使用in_()函数
                    valuation.code.in_(['000001.XSHE', '600000.XSHG'])
                ), date='2015-10-15')
            # 选出所有的总市值大于1000亿元, 市盈率小于10, 营业总收入大于200亿元的股票
            df = get_fundamentals(query(
                    valuation.code, valuation.market_cap, valuation.pe_ratio, income.total_operating_revenue
                ).filter(
                    valuation.market_cap > 1000,
                    valuation.pe_ratio < 10,
                    income.total_operating_revenue > 2e10
                ).order_by(
                    # 按市值降序排列
                    valuation.market_cap.desc()
                ).limit(
                    # 最多返回100个
                    100
                ), date='2015-10-15')
            # 使用 or_ 函数: 查询总市值大于1000亿元 **或者** 市盈率小于10的股票
            from sqlalchemy.sql.expression import or_
            get_fundamentals(query(
                    valuation.code
                ).filter(
                    or_(
                        valuation.market_cap > 1000,
                        valuation.pe_ratio < 10
                    )
                ))
            # 查询平安银行2014年四个季度的季报, 放到数组中
            q = query(
                    income.statDate,
                    income.code,
                    income.basic_eps,
                    balance.cash_equivalents,
                    cash_flow.goods_sale_and_service_render_cash
                ).filter(
                    income.code == '000001.XSHE',
                )

            rets = [get_fundamentals(q, statDate='2014q'+str(i)) for i in range(1, 5)]
            # 查询平安银行2014年的年报
            q = query(
                    income.statDate,
                    income.code,
                    income.basic_eps,
                    cash_flow.goods_sale_and_service_render_cash
                ).filter(
                    income.code == '000001.XSHE',
                )

            ret = get_fundamentals(q, statDate='2014')
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


def stock_get_fundamentals_continuously():
    """
    查询财务数据
    :财务数据列表 : https://www.joinquant.com/help/api/help?name=Stock#%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE%E5%88%97%E8%A1%A8
    :param :query_object: 一个sqlalchemy.orm.query.Query对象，可以通过全局的 query 函数获取 Query 对象，query简易教程。
            end_date: 查询日期, 一个字符串(格式类似'2015-10-15')或者[datetime.date]/[datetime.datetime]对象, 可以是None, 如果传入的 date 不是交易日, 则使用这个日期之前的最近的一个交易日
            count: 获取 end_date 前 count 个日期的数据
    :rtype :pandas.Panel
    :return:
    :其他实例
            q = query(valuation.turnover_ratio,
                      valuation.market_cap,
                      indicator.eps
                    ).filter(valuation.code.in_(['000001.XSHE', '600000.XSHG']))

        panel = get_fundamentals_continuously(q, end_date='2018-01-01', count=5)

        panel

        <class 'pandas.core.panel.Panel'>
        Dimensions: 3 (items) x 5 (major_axis) x 2 (minor_axis)
        Items axis: turnover_ratio to eps
        Major_axis axis: 2017-12-25 to 2017-12-29
        Minor_axis axis: 000001.XSHE to 600000.XSHG

        >>> panel.minor_xs('600000.XSHG')

        turnover_ratio  market_cap  eps
        day
        2017-12-25  0.0687  3695.4270   0.48
        2017-12-26  0.0542  3710.1030   0.48
        2017-12-27  0.1165  3704.2324   0.48
        2017-12-28  0.0849  3680.7510   0.48
        2017-12-29  0.0582  3695.4270   0.48


        >>> panel.major_xs('2017-12-25')

        turnover_ratio  market_cap  eps
        code
        000001.XSHE 0.9372  2275.0796   0.38
        600000.XSHG 0.0687  3695.4270   0.48

        >>> panel.xs('turnover_ratio',axis=0)
        # axis=0 表示 items axis; axis=1 表示 major axis; axis=2 表示 minor axis

        code    000001.XSHE 600000.XSHG
        day
        2017-12-25  0.9372  0.0687
        2017-12-26  0.6642  0.0542
        2017-12-27  0.8078  0.1165
        2017-12-28  0.9180  0.0849
        2017-12-29  0.5810  0.0582
    """
    q = query(valuation.turnover_ratio,
              valuation.market_cap,
              indicator.eps
              ).filter(valuation.code.in_(['000001.XSHE', '600000.XSHG']))

    panel = get_fundamentals_continuously(q, end_date='2018-01-01', count=5)
    df = panel.minor_xs('600000.XSHG')
    return df


"""
市值数据（每日更新）
每天更新，可以使用get_fundamentals(query(valuation),date),指定date为某一交易日,获取该交易日的估值数据。查询方法详见get_fundamentals()接口说明

表名: valuation

列名	列的含义	解释	公式
code	股票代码	带后缀.XSHE/.XSHG	
day	日期	取数据的日期	
capitalization	总股本(万股)	公司已发行的普通股股份总数(包含A股，B股和H股的总股本)	
circulating_cap	流通股本(万股)	公司已发行的境内上市流通、以人民币兑换的股份总数(A股市场的流通股本)	
market_cap	总市值(亿元)	A股收盘价*已发行股票总股本（A股+B股+H股）	
circulating_market_cap	流通市值(亿元)	流通市值指在某特定时间内当时可交易的流通股股数乘以当时股价得出的流通股票总价值。	A股市场的收盘价*A股市场的流通股数
turnover_ratio	换手率(%)	指在一定时间内市场中股票转手买卖的频率，是反映股票流通性强弱的指标之一。	换手率=[指定交易日成交量(手)100/截至该日股票的自由流通股本(股)]100%
pe_ratio	市盈率(PE, TTM)	每股市价为每股收益的倍数，反映投资人对每元净利润所愿支付的价格，用来估计股票的投资报酬和风险	市盈率（PE，TTM）=（股票在指定交易日期的收盘价 * 当日人民币外汇挂牌价* 截止当日公司总股本）/归属于母公司股东的净利润TTM。
pe_ratio_lyr	市盈率(PE)	以上一年度每股盈利计算的静态市盈率. 股价/最近年度报告EPS	市盈率（PE）=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/归属母公司股东的净利润。
pb_ratio	市净率(PB)	每股股价与每股净资产的比率	市净率=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/归属母公司股东的权益。
ps_ratio	市销率(PS, TTM)	市销率为股票价格与每股销售收入之比，市销率越小，通常被认为投资价值越高。	市销率TTM=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/营业总收入TTM
pcf_ratio	市现率(PCF, 现金净流量TTM)	每股市价为每股现金净流量的倍数	市现率=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/现金及现金等价物净增加额TTM
"""


"""

财务指标数据
按季度更新, 统计周期是一季度。可以使用get_fundamentals(query(indicator),date,statDate)查询，查询方法详见get_fundamentals()接口说明

表名: indicator

列名	列的含义	解释
code	股票代码	带后缀.XSHE/.XSHG
pubDate	日期	公司发布财报日期
statDate	日期	财报统计的季度的最后一天, 比如2015-03-31, 2015-06-30
eps	每股收益EPS(元)	每股收益(摊薄)＝净利润/期末股本；分子从单季利润表取值，分母取季度末报告期股本值。
adjusted_profit	扣除非经常损益后的净利润(元)	非经常性损益这一概念是证监会在1999年首次提出的，当时将其定义为：公司正常经营损益之外的一次性或偶发性损益。《问答第1号》则指出：非经常性损益是公司发生的与经营业务无直接关系的收支；以及虽与经营业务相关，但由于其性质、金额或发生频率等方面的原因，影响了真实公允地反映公司正常盈利能力的各项收入。
operating_profit	经营活动净收益(元)	营业总收入-营业总成本
value_change_profit	价值变动净收益(元)	公允价值变动净收益+投资净收益+汇兑净收益
roe	净资产收益率ROE(%)	归属于母公司股东的净利润*2/（期初归属于母公司股东的净资产+期末归属于母公司股东的净资产）
inc_return	净资产收益率(扣除非经常损益)(%)	扣除非经常损益后的净利润（不含少数股东损益）*2/（期初归属于母公司股东的净资产+期末归属于母公司股东的净资产）
roa	总资产净利率ROA(%)	净利润*2/（期初总资产+期末总资产）
net_profit_margin	销售净利率(%)	净利润/营业收入
gross_profit_margin	销售毛利率(%)	毛利/营业收入
expense_to_total_revenue	营业总成本/营业总收入(%)	营业总成本/营业总收入(%)
operation_profit_to_total_revenue	营业利润/营业总收入(%)	营业利润/营业总收入(%)
net_profit_to_total_revenue	净利润/营业总收入(%)	净利润/营业总收入(%)
operating_expense_to_total_revenue	营业费用/营业总收入(%)	营业费用/营业总收入(%)
ga_expense_to_total_revenue	管理费用/营业总收入(%)	管理费用/营业总收入(%)
financing_expense_to_total_revenue	财务费用/营业总收入(%)	财务费用/营业总收入(%)
operating_profit_to_profit	经营活动净收益/利润总额(%)	经营活动净收益/利润总额(%)
invesment_profit_to_profit	价值变动净收益/利润总额(%)	价值变动净收益/利润总额(%)
adjusted_profit_to_profit	扣除非经常损益后的净利润/归属于母公司所有者的净利润(%)	扣除非经常损益后的净利润/归属于母公司所有者的净利润(%)
goods_sale_and_service_to_revenue	销售商品提供劳务收到的现金/营业收入(%)	销售商品提供劳务收到的现金/营业收入(%)
ocf_to_revenue	经营活动产生的现金流量净额/营业收入(%)	经营活动产生的现金流量净额/营业收入(%)
ocf_to_operating_profit	经营活动产生的现金流量净额/经营活动净收益(%)	经营活动产生的现金流量净额/经营活动净收益(%)
inc_total_revenue_year_on_year	营业总收入同比增长率(%)	营业总收入同比增长率是企业在一定期间内取得的营业总收入与其上年同期营业总收入的增长的百分比，以反映企业在此期间内营业总收入的增长或下降等情况。
inc_total_revenue_annual	营业总收入环比增长率(%)	营业收入是指企业在从事销售商品，提供劳务和让渡资产使用权等日常经营业务过程中所形成的经济利益的总流入。环比增长率=（本期的某个指标的值-上一期这个指标的值）/上一期这个指标的值*100%。
inc_revenue_year_on_year	营业收入同比增长率(%)	营业收入,是指公司在从事销售商品、提供劳务和让渡资产使用权等日常经营业务过程中所形成的经济利益的总流入，而营业收入同比增长率，则是检验上市公司去年一年挣钱能力是否提高的标准，营业收入同比增长,说明公司在上一年度挣钱的能力加强了，营业收入同比下降，则说明公司的挣钱能力稍逊于往年。
inc_revenue_annual	营业收入环比增长率(%)	环比增长率=（本期的某个指标的值-上一期这个指标的值）/上一期这个指标的值*100%。
inc_operation_profit_year_on_year	营业利润同比增长率(%)	同比增长率就是指公司当年期的净利润和上月同期、上年同期的净利润比较。（当期的利润-上月（上年）当期的利润）/上月（上年）当期的利润=利润同比增长率。
inc_operation_profit_annual	营业利润环比增长率(%)	环比增长率=（本期的某个指标的值-上一期这个指标的值）/上一期这个指标的值*100%。
inc_net_profit_year_on_year	净利润同比增长率(%)	（当期的净利润-上月（上年）当期的净利润）/上月（上年）当期的净利润绝对值=净利润同比增长率。
inc_net_profit_annual	净利润环比增长率(%)	环比增长率=（本期的某个指标的值-上一期这个指标的值）/上一期这个指标的值*100%。
inc_net_profit_to_shareholders_year_on_year	归属母公司股东的净利润同比增长率(%)	归属于母公司股东净利润是指全部归属于母公司股东的净利润，包括母公司实现的净利润和下属子公司实现的净利润；同比增长率，一般是指和去年同期相比较的增长率。同比增长 和上一时期、上一年度或历史相比的增长（幅度）。
inc_net_profit_to_shareholders_annual	归属母公司股东的净利润环比增长率(%)	环比增长率=（本期的某个指标的值-上一期这个指标的值）/上一期这个指标的值*100%。

"""

q = query(valuation.turnover_ratio,
              valuation.market_cap,
              indicator.eps
            ).filter(valuation.code.in_(['000001.XSHE', '600000.XSHG']))

panel = get_fundamentals_continuously(q, end_date='2018-01-01', count=5)
df = panel.minor_xs('600000.XSHG')
print(df)