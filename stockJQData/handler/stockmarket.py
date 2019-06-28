#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-28 14:19
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : stockmarket.py
# @Software: PyCharm

from stockJQData.util import datau as du
from stockJQData.util import dataformat as dataf
from stockJQData.config import cons as ct
from stockJQData.UUStockData import stockMarketInfo as smi
from stockJQData.UUStockData import jqBase as jqb




def api_get_price(code,start_date,end_date,frequency):
    """
    :param code:
    :param start_date: '2019-05-28 14:47:48'
    :param end_date:   '2019-06-28 14:47:48'
    :param frequency:
    :return:
    """
    if frequency in ct.BAR_UNIT:
        code = jqb.uu_normalize_code(code)
        start_date = du.today_last_mon()
        end_date = du.get_hms()

        data = smi.uu_get_price(code, start_date, end_date, frequency)
        data['datetime'] = data.index
    else:
        raise TypeError('ktype input error.')
    datajson = dataf.data_to_json(data)
    return datajson

df = api_get_price('000001',1,1,'1m')
print(df)