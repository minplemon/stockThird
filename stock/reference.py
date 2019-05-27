#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-27 10:51
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : reference.py
# @Software: PyCharm

from stock import cons as ct




def profit_data(year=2017, top=25,retry_count=3,pause=0.001):
    """
    获取分配预案数据
    Parameters
    --------
    year:年份
    top:取最新n条数据，默认取最近公布的25条
    retry_count : int, 默认 3
                 如遇网络等问题重复执行的次数
      pause : int, 默认 0
                重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题

    returns
    -------
    DataFrame
    code:股票代码
    name:股票名称
    year:分配年份
    report_date:公布日期
    divi:分红金额（每10股）
    shares:转增和送股数（每10股）
    """
    if top == 'all':
        ct._write_head()




    return None