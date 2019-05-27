#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-22 14:15
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : dateu.py
# @Software: PyCharm

import datetime
import pandas as pd


def last_tddate():
    today = datetime.datetime.today().date()  # 2019-05-22
    today = int(today.strftime("%w"))  # 显示对于星期几 比如 2019-05-22 星期3
    if today == 0:
        return day_last_week(-2)
    else:
        return day_last_week(-1)


def today_last_year():
    lasty = datetime.datetime.today().date() + datetime.timedelta(-365)
    return str(lasty)


def today():
    day = datetime.datetime.today().date()
    return str(day)


def get_quarts(start, end):
    idx = pd.period_range('Q'.join(year_qua(start)), 'Q'.join(year_qua(end)),
                          freq='Q-JAN')
    return [str(d).split('Q') for d in idx][::-1]


def day_last_week(days=-7):
    lasty = datetime.datetime.today().date() + datetime.timedelta(-2)
    return str(lasty)


def year_qua(date):
    mon = date[5:7]
    mon = int(mon)
    return [date[0:4], _quar(mon)]


def _quar(mon):
    if mon in [1, 2, 3]:
        return '1'
    if mon in [4, 5, 6]:
        return '2'
    if mon in [7, 8, 9]:
        return '3'
    if mon in [10, 11, 12]:
        return '4'
    else:
        return None
