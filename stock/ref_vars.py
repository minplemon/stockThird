#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-27 14:04
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : ref_vars.py
# @Software: PyCharm

DP_URL = '%sapp.finance.%s/data/stock/%s?day=&page=%s'
DP_163_URL = '%squotes.%s/data/caibao/%s?reportdate=%s&sort=declaredate&order=desc&page=%s'
DP_163_COLS = ['code', 'name', 'year', 'plan', 'report_date']