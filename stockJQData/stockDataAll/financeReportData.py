#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-19 17:09
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : financeReportData.py
# @Software: PyCharm

# 报告期财务数据是上市公司定期公告中按照报告期统计的财务数据
from jqdatasdk import *
auth('18620668927', 'minpeng123')   # 账号密码认证



ss = get_mtss('000001.XSHE', '2016-01-01', '2016-04-01')
print(ss)