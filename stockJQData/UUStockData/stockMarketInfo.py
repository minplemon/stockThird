#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-19 14:54
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : stockMarketInfo.py
# @Software: PyCharm


"""
##   获取交易行情数据
###  get_trade_days - 获取指定范围交易日
     get_all_trade_days - 获取所有交易日
     get_price - 获取行情数据
     get_bars - 获取指定时间周期的行情数据
     get_mtss - 获取融资融券信息
     get_money_flow - 获取资金流向信息
     get_billboard_list - 获取龙虎榜数据
    *get_future_contracts-获取期货可交易合约列表
    *get_dominant_future-获取主力合约对应的标的
参考 https://www.joinquant.com/help/api/help?name=JQData#%E8%8E%B7%E5%8F%96%E4%BA%A4%E6%98%93%E8%A1%8C%E6%83%85%E6%95%B0%E6%8D%AE
"""
from jqdatasdk import *
auth('18620668927', 'minpeng123')   # 账号密码认证






def uu_get_ticks():
    """
    获取股票 tick 数据 (历史数据)
    :param :security: 股票代码或期货代码
            end_dt: 结束日期
            start_dt: 开始日期, 与count参数二选一
            count: 取出指定时间区间内前多少条的tick数据, 与start_dt参数二选一
            fields: 选择要获取的行情数据字段，默认为["time", "current", "high", "low", "volume", "money"]
    :rtype : numpy.ndarray
    :return:    字段名	说明	字段类型
                time	时间	float
                current	当前价	float
                high	当日最高价	float
                low	当日最低价	float
                volume	累计成交量	float
                money	累计成交额	float
                a1_v~a5_v	五档卖量	float
                a1_p~a5_p	五档卖价	float
                b1_v~b5_v	五档买量	float
                b1_p~b5_p	五档买价	float
    """
    return get_ticks("000001.XSHE",start_dt="2019-06-19", end_dt="2019-06-21")


def uu_get_current_tick(stock):
    """
    获取单支股票实时行情
    :param :security: 标的代码， 支持股票、商品期货和股指期货以及包含标的代码的列表。 期货需要使用具体合约代码，不可以使用主力合约和指数合约代码
    :rtype :
    :return:当传入参数为标的代码时，返回tick 对象；当传入包含标的代码的列表则返回一个dict，key是标的代码，value和传入一个字符串的返回值一样
    """
    return get_current_tick(stock)

def uu_get_trade_days():
    """
    获取指定范围交易日
    获取指定日期范围内的所有交易日, 返回 [numpy.ndarray], 包含指定的 start_date 和 end_date, 默认返回至 datatime.date.today() 的所有交易日
    :param :start_date: 开始日期, 与 count 二选一, 不可同时使用. str/[datetime.date]/[datetime.datetime] 对象
            end_date: 结束日期, str/[datetime.date]/[datetime.datetime] 对象, 默认为 datetime.date.today()
            count: 数量, 与 start_date 二选一, 不可同时使用, 必须大于 0. 表示取 end_date 往前的 count 个交易日，包含 end_date 当天。
    :rtype :numpy.ndarray
    :return:
    """
    return get_trade_days(start_date="2019-01-01", end_date="2020-01-01")

def uu_get_all_trade_days():
    """
    获取所有交易日, 不需要传入参数, 返回一个包含所有交易日的 [numpy.ndarray], 每个元素为一个 [datetime.date] 类型.
    :param :
    :rtype :
    :return:
    """
    return get_all_trade_days()

def uu_get_price(stock,start_date,end_date,frequency='1m'):
    """
    获取一支或者多只股票的实时行情和历史行情, 按天或者按分钟，这里在使用时注意 end_date 的设置，不要引入未来的数据
    :param :security: 一支股票代码或者一个股票代码的list

            count: 与 start_date 二选一，不可同时使用. 数量, 返回的结果集的行数, 即表示获取 end_date 之前几个 frequency 的数据

            start_date: 与 count 二选一，不可同时使用. 字符串或者 [datetime.datetime]/[datetime.date] 对象, 开始时间.

            如果 count 和 start_date 参数都没有, 则 start_date 生效, 值是 '2015-01-01'. 注意:
            当取分钟数据时, 时间可以精确到分钟, 比如: 传入 datetime.datetime(2015, 1, 1, 10, 0, 0) 或者 '2015-01-01 10:00:00'.
            当取分钟数据时, 如果只传入日期, 则日内时间是当日的 00:00:00.
            当取天数据时, 传入的日内时间会被忽略
            end_date: 格式同上, 结束时间, 默认是'2015-12-31', 包含此日期. 注意: 当取分钟数据时, 如果 end_date 只有日期, 则日内时间等同于 00:00:00, 所以返回的数据是不包括 end_date 这一天的.

            frequency: 单位时间长度, 几天或者几分钟, 现在支持'Xd','Xm', 'daily'(等同于'1d'), 'minute'(等同于'1m'), X是一个正整数, 分别表示X天和X分钟(不论是按天还是按分钟回测都能拿到这两种单位的数据), 注意, 当X > 1时, fields只支持['open', 'close', 'high', 'low', 'volume', 'money']这几个标准字段. 默认值是daily

            fields: 字符串list, 选择要获取的行情数据字段, 默认是None(表示['open', 'close', 'high', 'low', 'volume', 'money']这几个标准字段), 支持SecurityUnitData里面的所有基本属性,，包含：['open', 'close', 'low', 'high', 'volume', 'money', 'factor', 'high_limit','low_limit', 'avg', 'pre_close', 'paused']

            skip_paused: 是否跳过不交易日期(包括停牌, 未上市或者退市后的日期). 如果不跳过, 停牌时会使用停牌前的数据填充(具体请看SecurityUnitData的paused属性), 上市前或者退市后数据都为 nan, 但要注意:

            默认为 False
            当 skip_paused 是 True 时, 只能取一只股票的信息 关于停牌: 因为此API可以获取多只股票的数据, 可能有的股票停牌有的没有, 为了保持时间轴的一致,我们默认没有跳过停牌的日期, 停牌时使用停牌前的数据填充(请看 [SecurityUnitData] 的 paused 属性). 如想跳过, 请使用 skip_paused=True 参数, 同时只取一只股票的信息
            fq: 复权选项:

            'pre': 前复权
            None: 不复权, 返回实际价格
            'post': 后复权
    :rtype :
    :return:
    """
    return get_price(stock, start_date=start_date, end_date=end_date, frequency=frequency,
               fields=['open', 'close','low','high','volume','money','factor','high_limit','low_limit','avg','pre_close','paused'])


def uu_get_bars():
    """
    获取各种时间周期的bar数据，bar的分割方式与主流股票软件相同， 同时还支持返回当前时刻所在 bar 的数据
    :param :security: 股票代码，支持单个及多个标的
            count: 大于0的整数，表示获取bar的个数。如果行情数据的bar不足count个，返回的长度则小于count个数。
            unit: bar的时间单位, 支持如下周期：'1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', '1M'。其中m表示分钟，d表示天，w表示周，M表示月。
            fields: 获取数据的字段， 支持如下值：'date', 'open', 'close', 'high', 'low', 'volume', 'money'。
            include_now: 取值True 或者False。 表示是否包含当前bar, 比如策略时间是9:33，unit参数为5m， 如果 include_now=True,则返回9:30-9:33这个分钟 bar。
            end_dt：查询的截止时间，支持的类型为datetime.datetime或None，默认为datetime.now()。
            fq_ref_date：复权基准日期，为None时为不复权数据。
    :rtype :pandas.dataframe
    :return:
    """
    return get_bars('600519.XSHG', 10, unit='1d',fields=['date','open','high','low','close'],include_now=False,end_dt='2018-12-05')

def uu_get_mtss():
    """
    获取一只或者多只股票在一个时间段内的融资融券信息
    :param :security_list: 一只股票代码或者一个股票代码的 list

            start_date: 开始日期, 与 count 二选一, 不可同时使用. 一个字符串或者 [datetime.datetime]/[datetime.date] 对象, 默认为平台提供的数据的最早日期

            end_date: 结束日期, 一个字符串或者 [datetime.date]/[datetime.datetime] 对象, 默认为 datetime.date.today()

            count: 数量, 与 start_date 二选一，不可同时使用, 必须大于 0. 表示返回 end_date 之前 count 个交易日的数据, 包含 end_date

            fields: 字段名或者 list, 可选. 默认为 None, 表示取全部字段, 各字段含义如下：

            字段名	含义
            date	日期
            sec_code	股票代码
            fin_value	融资余额(元）
            fin_buy_value	融资买入额（元）
            fin_refund_value	融资偿还额（元）
            sec_value	融券余量（股）
            sec_sell_value	融券卖出量（股）
            sec_refund_value	融券偿还量（股）
            fin_sec_value	融资融券余额（元）
    :rtype :pandas.DataFrame
    :return:
    """
    return get_mtss('000001.XSHE', '2016-01-01', '2016-04-01')

def uu_get_money_flow():
    """
    获取一只或者多只股票在一个时间段内的资金流向数据
    :param :security_list: 一只股票代码或者一个股票代码的 list
            start_date: 开始日期, 一个字符串或者 [datetime.datetime]/[datetime.date] 对象
            end_date: 结束日期, 一个字符串或者 [datetime.date]/[datetime.datetime] 对象
            count: 数量, 与 start_date 二选一，不可同时使用, 必须大于 0. 表示返回 end_date 之前 count 个交易日的数据, 包含 end_date
            fields: 字段名或者 list, 可选. 默认为 None, 表示取全部字段, 各字段含义如下：
            字段名	含义	备注
            date	日期
            sec_code	股票代码
            change_pct	涨跌幅(%)
            net_amount_main	主力净额(万)	主力净额 = 超大单净额 + 大单净额
            net_pct_main	主力净占比(%)	主力净占比 = 主力净额 / 成交额
            net_amount_xl	超大单净额(万)	超大单：大于等于50万股或者100万元的成交单
            net_pct_xl	超大单净占比(%)	超大单净占比 = 超大单净额 / 成交额
            net_amount_l	大单净额(万)	大单：大于等于10万股或者20万元且小于50万股或者100万元的成交单
            net_pct_l	大单净占比(%)	大单净占比 = 大单净额 / 成交额
            net_amount_m	中单净额(万)	中单：大于等于2万股或者4万元且小于10万股或者20万元的成交单
            net_pct_m	中单净占比(%)	中单净占比 = 中单净额 / 成交额
            net_amount_s	小单净额(万)	小单：小于2万股或者4万元的成交单
            net_pct_s	小单净占比(%)	小单净占比 = 小单净额 / 成交额
    :rtype :pandas.DataFrame
    :return:
    """
    return get_money_flow('000001.XSHE', '2016-02-01', '2016-02-04')


def uu_get_billboard_list(stock_list=None, end_date = '2019-06-20' ):
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
    return get_billboard_list(stock_list=stock_list, end_date = end_date, count =1)

def uu_get_future_contracts():
    """
    获取某期货品种在指定日期下的可交易合约标的列表
    :param :security: 期货合约品种，如 'AG'(白银)
            date：指定日期，默认为None，不指定时返回当前日期下可交易的合约标的列表
    :rtype :
    :return:
    """
    return get_future_contracts('AU','2017-01-05')

def uu_get_dominant_future():
    """
    获取主力合约对应的标的
    :param :underlying_symbol: 期货合约品种，如 'AG'(白银)
            dt:指定日期参数，获取历史上该日期的主力期货合约
    :rtype :
    :return:
    """
    return get_dominant_future('AU','2018-05-06')


# df = uu_get_ticks()
# print(df)