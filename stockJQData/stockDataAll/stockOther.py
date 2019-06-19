#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-19 15:16
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : stockOther.py
# @Software: PyCharm

# 获取行情数据
from jqdatasdk import *
auth('18620668927', 'minpeng123')   # 账号密码认证

def uu_get_margincash_stocks():
    """
    获取融资标的列表
    :param :date:默认为None,不指定时返回上交所、深交所最近一次披露的的可融资标的列表的list
    :rtype : list
    :return:返回指定日期上交所、深交所披露的的可融资标的列表的list
    """
    return get_margincash_stocks()


def uu_get_marginsec_stocks():
    """
    获取融券标的列表
    :param :date:默认为None,不指定时返回上交所、深交所最近一次披露的的可融券标的列表的list
    :rtype : list
    :return:返回指定日期上交所、深交所披露的的可融券标的列表的list
    """
    return get_marginsec_stocks()

def uu_get_billboard_list():
    """
    获取指定日期区间内的龙虎榜数据
    :param :stock_list: 一个股票代码的 list。 当值为 None 时， 返回指定日期的所有股票。
            start_date:开始日期
            end_date: 结束日期
            count: 交易日数量， 可以与 end_date 同时使用， 表示获取 end_date 前 count 个交易日的数据(含 end_date 当日)
    :rtype : pandas.DataFrame
    :return:code: 股票代码
            day: 日期
            direction: ALL 表示『汇总』，SELL 表示『卖』，BUY 表示『买』
            abnormal_code: 异常波动类型
            abnormal_name: 异常波动名称
            sales_depart_name: 营业部名称
            rank: 0 表示汇总， 1~5 对应买入金额或卖出金额排名第一到第五
            buy_value:买入金额
            buy_rate:买入金额占比(买入金额/市场总成交额)
            sell_value:卖出金额
            sell_rate:卖出金额占比(卖出金额/市场总成交额)
            net_value:净额(买入金额 - 卖出金额)
            amount:市场总成交额
    :异常波动类型 :
            106001	涨幅偏离值达7%的证券
            106002	跌幅偏离值达7%的证券
            106003	日价格振幅达到15%的证券
            106004	换手率达20%的证券
            106005	无价格涨跌幅限制的证券
            106006	连续三个交易日内收盘价格涨幅偏离值累计达到20%的证券
            106007	连续三个交易日内收盘价格跌幅偏离值累计达到20%的证券
            106008	连续三个交易日内收盘价格涨幅偏离值累计达到15%的证券
            106009	连续三个交易日内收盘价格跌幅偏离值累计达到15%的证券
            106010	连续三个交易日内涨幅偏离值累计达到12%的ST证券、*ST证券和未完成股改证券
            106011	连续三个交易日内跌幅偏离值累计达到12%的ST证券、*ST证券和未完成股改证券
            106012	连续三个交易日的日均换手率与前五个交易日日均换手率的比值到达30倍
            106013	单只标的证券的当日融资买入数量达到当日该证券总交易量的50％以上的证券
            106014	单只标的证券的当日融券卖出数量达到当日该证券总交易量的50％以上的证券
            106099	其它异常波动的证券
    """
    return get_billboard_list(stock_list=None, end_date = '2018-08-01', count =1)

def uu_get_locked_shares():
    """
    获取指定日期区间内的限售解禁数据
    :param :stock_list: 一个股票代码的 list
            start_date: 开始日期
            end_date: 结束日期
            forward_count: 交易日数量， 可以与 start_date 同时使用， 表示获取 start_date 到 forward_count 个交易日区间的数据
    :rtype :pandas.DataFrame
    :return:pandas.DataFrame， 各 column 的含义如下:
            day: 解禁日期
            code: 股票代码
            num: 解禁股数
            rate1: 解禁股数/总股本
            rate2: 解禁股数/总流通股本
    """
    return get_locked_shares(stock_list=['000001.XSHE', '000002.XSHE'], start_date='2018-08-01', forward_count=500)

ss = get_locked_shares(stock_list=['000001.XSHE', '000002.XSHE'], start_date='2018-08-01', forward_count=500)
print(ss)