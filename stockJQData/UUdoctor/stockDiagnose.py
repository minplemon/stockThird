#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-21 16:00
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : stockDiagnose.py
# @Software: PyCharm

import datetime

from stockJQData.UUStockData import stockBaseInfo as sbi
from stockJQData.UUStockData import stockMarketInfo as smi
from stockJQData.UUStockData import tushareStockBasics as tssb
from stockJQData.UUStockData import factors as factors
from stockJQData.UUStockData import listedCompanyInfo as lci
from stockJQData.UUStockData import stockIndustryConcept as sic
from stockJQData.UUStockData import listedCompanyShareholderInfo as lcsi  # 获取上市公司股东和股本信息
from stockJQData.UUStockData import stockOther as so
from stockJQData.UUStockData import financeDateData as fdd
from stockJQData.UUStockData import financeReportData as frd


today = datetime.datetime.today().date()  # 2019-06-21


stockName = sbi.uu_get_security_info('000001.XSHE')         # 获取股票信息
stockOpenClose = smi.uu_get_price('000001.XSHE', today, today)  # 获取开盘信息
currentPrice = smi.uu_get_current_tick('000001.XSHE')                # 获取实时价格
stockSort = tssb.uu_get_sort()                                    # 市场排名 按照市盈利排序
# differenceValue = currentPrice['current'] - stockOpenClose['open']   # 开盘涨跌额

setBooks = factors.uu_get_factor_values(
    '000001.XSHE', today, today)  # 必读  净资产收益率还没有

stk_list = lci.uu_query_STK_LIST('000001.XSHE')  # 股票上市信息
belongIndustry = sic.uu_get_industry('000001.XSHE', today)    # 所属行业
stk_company_info = lci.uu_query_STK_COMPANY_INFO('000001.XSHE')  # 公司最新公布的基本信息

participationInProfit = so.uu_query_STK_XR_XD('000001.XSHE')  # 获取分红

lci.uu_query_STK_MANAGEMENT_INFO('000001.XSHE')  # 公司高管

lcsi.uu_query_STK_HOLDER_NUM('000001.XSHE', '2015-01-01')  # 股东人数
lcsi.uu_query_STK_SHAREHOLDER_FLOATING_TOP10('000001.XSHE')  # 十大流通股东

fdd.uu_get_fundamentals('000001.XSHE')  # 总股本 流通股本

frd.uu_query_STK_INCOME_STATEMENT('000001.XSHE')  # 利润表
frd.uu_query_STK_BALANCE_SHEET('000001.XSHE')  # 合并资产负债表
frd.uu_query_STK_CASHFLOW_STATEMENT('000001.XSHE')  # 合并现金流量表
print(str)
