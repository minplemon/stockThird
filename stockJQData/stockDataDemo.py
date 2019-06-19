#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-19 14:05
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : stockDataDemo.py
# @Software: PyCharm

## 诊股详情
from jqdatasdk import *
auth('18620668927', 'minpeng123')   # 账号密码认证

d = get_ticks("000001.XSHE",start_dt=None, end_dt="2018-07-02", count=10)
print(d)