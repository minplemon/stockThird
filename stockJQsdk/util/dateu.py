#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-28 14:21
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : dateu.py
# @Software: PyCharm

import datetime


def get_today():
    """
    # 2019-06-21
    :return:
    """
    today = datetime.datetime.today().date()
    return str(today)


def get_hms():
    """
    '2019-06-28 14:47:48'
    :return:
    """
    hms = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    return str(hms)


def today_last_year():
    lasty = datetime.datetime.today().date() + datetime.timedelta(-365)
    return str(lasty)


def last_tddate():
    today = datetime.datetime.today().date()  # 2019-05-22
    today = int(today.strftime("%w"))  # 显示对于星期几 比如 2019-05-22 星期3
    return str(today)
