#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-19 14:20
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : UUStockDiagnoseData.py
# @Software: PyCharm

## 诊股详情
from jqdatasdk import *
auth('18620668927', 'minpeng123')   # 账号密码认证

def uu_get_industry():
    """
    查询股票所属行业
    :param :security：标的代码，类型为字符串，形式如"000001.XSHE"；或为包含标的代码字符串的列表，形如["000001.XSHE", "000002.XSHE"]
            date：查询的日期。类型为字符串，形如"2018-06-01"或"2018-06-01 09:00:00"；或为datetime.datetime对象和datetime.date。注意传入对象的时分秒将被忽略
    :rtype :dict
    :return:
    """
    return get_industry("600519.XSHG",date="2018-06-01")