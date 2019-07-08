#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-08 14:13
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : getOnePrice.py
# @Software: PyCharm

# 如不指定下载数据的时间段,则自动判断下载全量或补充增量,
# 如指定下载数据时间段,则删除期间数据,重新下载全部股票的数据

import sys
import datetime
import pandas as pd
import jqdatasdk as jq
import mysql.connector
import pymysql
from sqlalchemy import create_engine


def get_one_price(security, startday, endday):
    '''获取单只股票的指定时间段的后复权日线数据'''
    res = jq.get_price(
        security,
        start_date=startday,
        end_date=endday,
        frequency='daily',
        fields=[
            'open',
            'close',
            'high',
            'low',
            'volume',
            'money',
            'factor',
            'high_limit',
            'low_limit',
            'avg',
            'pre_close',
            'paused'],
        skip_paused=False,
        fq='post',
        count=None)
    '''增加股票代码列'''
    res['security'] = security
    print(res)

    '''表路由,计算表名'''
    tmod = int(security[:6]) % 5

    tablename = 't_kline_day_' + str(tmod)
    print(tablename)

    '''清理老数据'''
    sql = "delete from " + tablename + " where security = '" + security + \
        "' and kday >='" + startday + "' and kday <='" + endday + "'"
    print(sql)
    mdbconn = mysql.connector.connect(
        user='root',
        password='12345678',
        database='jqdata',
        use_unicode=True)
    cursor = mdbconn.cursor()
    cursor.execute(sql)
    mdbconn.commit()
    cursor.close()

    '''DataFrame入库'''
    pymysql.install_as_MySQLdb()
    mysqlconnect = create_engine(
        'mysql+mysqldb://jqdata:jqdata@localhost:3306/jqdata?charset=utf8')
    res.to_sql(
        name=tablename,
        con=mysqlconnect,
        schema='jqdata',
        if_exists='append',
        index=True,
        index_label='kday',
        chunksize=1000)
    print("all " + security + "data saved in " + tablename + " success")
    return


def get_all_price(b='0', e='0'):
    '''遍历全部股票,获取日线数据'''
    '''从本地数据库里获取全部股票信息,代码,上市日期,退市日期'''
    mdbconn = mysql.connector.connect(
        user='root',
        password='12345678',
        database='jqdata',
        use_unicode=True)
    sql = "select security , start_date, end_date from t_all_securities"

    securities = pd.read_sql(
        sql,
        mdbconn,
        index_col=None,
        coerce_float=True,
        params=None,
        parse_dates=None,
        columns=None,
        chunksize=None)

    cursor = mdbconn.cursor()
    for i in range(0, len(securities)):
        security = securities.iloc[i]['security']
        # 没有入参,表示自动运行,判断已经存在的数据,加载至今的,没有数据,加载全部数据.
        if b == '0':
            startday = securities.iloc[i]['start_date'].strftime('%Y-%m-%d')
            endday = securities.iloc[i]['end_date'].strftime('%Y-%m-%d')

            tmod = int(security[:6]) % 5

            tablename = 't_kline_day_' + str(tmod)

            sql = "select ifnull(max(kday),'0000-00-00') as kday from " + \
                tablename + " where security = '" + security + "'"

            cursor.execute(sql)
            kday = cursor.fetchone()[0]

            today = datetime.datetime.now().strftime('%Y-%m-%d')

            # 计算起始日期
            if kday == '0000-00-00':
                pass
            elif kday != '0000-00-00' and kday < today:
                delta = datetime.timedelta(days=1)
                kday = datetime.datetime.strptime(kday, '%Y-%m-%d')
                startday = (kday + delta).strftime('%Y-%m-%d')

            # 计算结束日期
            if today < endday:
                endday = today

        else:
            # 按指定日期运行
            startday = b
            endday = e

        get_one_price(security, startday, endday)

    cursor.close()
    return


def main(b='0', e='0'):
    jq.auth('***', '***')

    get_all_price(b, e)

    jq.logout()


if __name__ == "__main__":
    # sys.exit(main())
    sys.exit(main('2019-07-01', '2019-07-02'))
