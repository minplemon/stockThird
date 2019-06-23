#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-20 18:00
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : fundOtc.py
# @Software: PyCharm


"""
##   场外基金数据
###  获取公募基金主体信息
     获取基金净值信息
     获取基金持股信息（按季度公布）
     获取基金资产组合概况
     获取基金持有的债券信息
     获取基金财务信息
     获取基金收益日报
     获取基金分红拆分合并信息
参考 https://www.joinquant.com/help/api/help?name=JQData#%E5%9C%BA%E5%A4%96%E5%9F%BA%E9%87%91%E6%95%B0%E6%8D%AE
"""
from jqdatasdk import *
auth('18620668927', 'minpeng123')   # 账号密码认证

