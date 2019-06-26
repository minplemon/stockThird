#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-26 10:33
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : pddata.py
# @Software: PyCharm

from pandas_datareader import data
import matplotlib.pyplot as plt
import datetime
import pandas as pd


# 简单案例1
stock_code = input("美股直接输入股票代码如GOOG \n港股输入代码+对应股市，如腾讯：0700.hk \n国内股票需要区分上证和深证，股票代码后面加.ss或者.sz\n请输入你要查询的股票代码：")
start_date = "2019-06-20"
end_date = "2019-06-26"
stock_info = data.get_data_yahoo(stock_code, start_date, end_date)
# 展示前5行
print(stock_info.head())
# print(stock_info.info())
#  保存为Excel文件和CSV文件
# stock_info.to_excel('%s.xlsx'%stock_code)
# stock_info.to_csv('%s.csv'%stock_code)
# 输出图表
plt.plot(stock_info['Close'], 'g')
plt.show()

# 简单案例2
start = datetime.datetime(2019, 1, 2) # or start = '2/1/2019'
end = datetime.date.today()
prices = data.DataReader('AAPL', 'yahoo', start, end)  # 得到AApl的股票数据
prices.head()  # print first rows of the prices data


"""
参考链接 https://blog.csdn.net/weixin_44510615/article/details/89528712
"""