#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-26 18:14
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : getdata.py
# @Software: PyCharm

import pandas as pd
import jqdatasdk as jq
import stockJQData.localjq.modeldata as md
import datetime as dt


jq.auth('***', '***')
data = jq.get_all_securities(types=[], date=None)
for i, r in data.iterrows():
    d = jq.get_price(r.code, start_date=dt.datetime(2018, 1, 1), end_date=dt.datetime(2018, 10, 30),
                            frequency='daily', fields=None, skip_paused=False, fq='pre', count=None)
    # 这里，其实你还可以对d进行一些调整
    # 将d插入数据库中，md()括号中不传参数，就会插入到默认的那个数据库中==>"default"
    md().insert_data(table_name='kline_day', data=d)
    # 当你要把d插入到另一个数据库中，则需要在md()中传入参数，像这样：
    # md(location='server1').insert_data(table_name='kline_day', data=d) # 'server1'我们在数据库配置那个json中见过的