#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-28 14:21
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : dateu.py
# @Software: PyCharm

import datetime as dt
import re


def get_today():
    """
    # 2019-06-21
    :return:
    """
    today = dt.datetime.today().date()
    return str(today)


def get_hms():
    """
    '2019-06-28 14:47:48'
    :return:
    """
    hms = dt.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    return str(hms)


def today_last_year():
    lasty = dt.datetime.today().date() + dt.timedelta(-365)
    return str(lasty)

def today_last_mon():
    lastm = dt.datetime.today().date() + dt.timedelta(-30)
    return str(lastm)


def last_tddate():
    today = dt.datetime.today().date()  # 2019-05-22
    today = int(today.strftime("%w"))  # 显示对于星期几 比如 2019-05-22 星期3
    return str(today)


def parse_date(date_str):
    try:
        if not date_str:
            return None
        if "-" in date_str:
            if date_str.count("-") == 1:
                date_str = re.compile(r"\d+-\d+").search(date_str).group()
                date = dt.datetime.strptime(date_str, "%Y-%m")
            elif date_str.count("-") == 2:
                date_str = re.compile(r"\d+-\d+-\d+").search(date_str).group()
                date = dt.datetime.strptime(date_str, "%Y-%m-%d")
        elif "年" in date_str:
            if "日" in date_str:
                date_str = re.compile(r"\d+年\d+月\d+日").search(date_str).group()
                date = dt.datetime.strptime(date_str, "%Y年%m月%d日")
            elif "月" in date_str:
                date_str = re.compile(r"\d+年\d+月").search(date_str).group()
                date = dt.datetime.strptime(date_str, "%Y年%m月")
            else:
                date_str = re.compile(r"\d+年").search(date_str).group()
                date = dt.datetime.strptime(date_str, "%Y年")
        elif date_str.isdigit():
            if len(date_str) == 4:
                date = dt.datetime.strptime(date_str, "%Y")
            elif len(date_str) > 6:
                date = dt.datetime.strptime(date_str, "%Y%m%d")
            else:
                date = dt.datetime.strptime(date_str, "%Y%m")
        else:
            date = None
    except:
        return None
    return date


# str ='2019-06-28 14:47:48'
# # 正则去掉多余的
# kk =parse_date(str)
# print(kk)