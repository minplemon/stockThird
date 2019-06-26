#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-21 17:08
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : tushareStockBasics.py
# @Software: PyCharm

import numpy as np
import tushare as ts
import pandas as pd


pro = ts.pro_api()

def uu_get_sort(sort='pe'):
    """
    默认按照市盈利排序
    :param sort:
    :rtype :DataFrame
    :return:
    """
    df2 = ts.get_stock_basics()
    df3 = df2.sort_values(by=sort, ascending=False)
    df4 = pd.Series(np.arange(1, len(df3) + 1), name='sort', index=df3.index)
    df5 = pd.concat([df3, df4], axis=1)
    return df5

def uu_top_list():
    df = pro.top_list(trade_date='20180928')
    return df

