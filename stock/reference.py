#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-27 10:51
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : reference.py
# @Software: PyCharm


from __future__ import division
from stock import cons as ct
from stock import ref_vars as rv
import pandas as pd
import numpy as np
import time
import lxml.html
from lxml import etree
import re
import json
from pandas.compat import StringIO
from util import dateu as du
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request


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
        df,pages = _dist_cotent(year,0,retry_count,pause)
        for idx in range(1,int(pages)):
            df = df.append(_dist_cotent(year,idx,retry_count,pause),ignore_index=True)
            return df
    elif top <= 25:
        df, pages = _dist_cotent(year,0,retry_count,pause)
        return df.head(top)
    else:
        if isinstance(top, int):
            ct._write_head()
            allPages = top/25+1 if top%25 else top/25
            df, pages = _dist_cotent(year,0,retry_count,pause)
            if int(allPages) < int(pages):
                pages = allPages
            for idx in range(1,int(pages)):
                df = df.append(_dist_cotent(year,idx,retry_count,pause),ignore_index=True)
            return df.head(top)
        else:
            print(ct.NETWORK_URL_ERROR_MSG)



def _dist_cotent(year,pageNo,retry_count,pause):
    for _ in range(retry_count):
        time.sleep(retry_count)
        try:
            if pageNo > 0:
                ct._write_console()
            html = lxml.html.parse(rv.DP_163_URL%(ct.P_TYPE['http'],ct.DOMAINS['163'],
                                                  ct.PAGES['163dp'],year,pageNo))
            res = html.xpath('//div[@class=\"fn_rp_list\"]/table')
            if ct.PY3:
                sarr = [etree.tostring(node).decode('utf-8') for node in res]
            else:
                sarr =[etree.tostring(node) for node in res]
            sarr = ''.join(sarr)
            df = pd.read_html(sarr, skiprows=[0])[0]
            df = df.drop(df.columns[0], axis=1)
            df.columns = rv.DP_163_COLS
            df['divi'] = df['plan'].map(_fun_divi)
            df['shares'] = df['plan'].map(_fun_into)
            df['code'] = df['code'].astype(object)
            df['code'] = df['code'].map(lambda x: str(x).zfill(6))
            pages =[]
            if pageNo == 0:
                page = html.xpath('//div[@class=\"mod_pages\"]/a')
                if len(page) >1:
                    asr = page[len(page)-2]
                    pages = asr.xpath('text()')
        except Exception as e:
            print(e)
        else:
            if pageNo == 0:
                return df, pages[0] if len(pages)>0 else 0
            else:
                return df
    raise IOError(ct.NETWORK_URL_ERROR_MSG)







    return None


def _fun_divi(x):
    if ct.PY3:
        reg = re.compile(r'分红(.*?)元', re.UNICODE)
        res = reg.findall(x)
        return 0 if len(res)<1 else float(res[0])
    else:
        if isinstance(x, str):
            s1 = str('分红','utf-8')
            s2 = str('元','utf-8')
            reg = re.compile(r'%s(.*?)%s'%(s1, s2), re.UNICODE)
            res = reg.findall(x)
            return 0 if len(res)<1 else float(res[0])
        else:
            return 0

def _fun_into(x):
    if ct.PY3:
            reg1 = re.compile(r'转增(.*?)股', re.UNICODE)
            reg2 = re.compile(r'送股(.*?)股', re.UNICODE)
            res1 = reg1.findall(x)
            res2 = reg2.findall(x)
            res1 = 0 if len(res1)<1 else float(res1[0])
            res2 = 0 if len(res2)<1 else float(res2[0])
            return res1 + res2
    else:
        if isinstance(x, str):
            s1 = str('转增','utf-8')
            s2 = str('送股','utf-8')
            s3 = str('股','utf-8')
            reg1 = re.compile(r'%s(.*?)%s'%(s1, s3), re.UNICODE)
            reg2 = re.compile(r'%s(.*?)%s'%(s2, s3), re.UNICODE)
            res1 = reg1.findall(x)
            res2 = reg2.findall(x)
            res1 = 0 if len(res1)<1 else float(res1[0])
            res2 = 0 if len(res2)<1 else float(res2[0])
            return res1 + res2
        else:
            return 0