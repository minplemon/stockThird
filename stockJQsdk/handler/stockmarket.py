#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-28 14:19
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : stockmarket.py
# @Software: PyCharm

from stockJQData.UUStockData import stockMarketInfo as smi
from stockJQData.util import datau as du

smi.uu_get_price(du.today_last_year(),du.get_hms(),)