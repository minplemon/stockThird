#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-20 18:00
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : fundOn.py
# @Software: PyCharm

"""
##   获取场内基金份额数据
###  获取场内基金份额数据
参考  https://www.joinquant.com/help/api/help?name=JQData#%E8%8E%B7%E5%8F%96%E5%9C%BA%E5%86%85%E5%9F%BA%E9%87%91%E4%BB%BD%E9%A2%9D%E6%95%B0%E6%8D%AE
"""
from jqdatasdk import *
auth('18620668927', 'minpeng123')   # 账号密码认证



#查询2019-05-23的场内基金份额数据
df=finance.run_query(query(finance.FUND_SHARE_DAILY).filter(finance.FUND_SHARE_DAILY.date=='2019-05-23').limit(10))
print(df)