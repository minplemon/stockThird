#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-19 17:06
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : maketTong.py
# @Software: PyCharm

# 市场通
from jqdatasdk import *
auth('18620668927', 'minpeng123')   # 账号密码认证



ss = get_mtss('000001.XSHE', '2016-01-01', '2016-04-01')
print(ss)