#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-08 14:14
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : getOnedayValuation.py
# @Software: PyCharm

# 获取市值数据,入参是日期,每日获取全部数据

import sys
import datetime
import pandas as pd
import jqdatasdk as jq
from jqdatasdk import *
import mysql.connector
import pymysql
import sqlalchemy
from sqlalchemy import create_engine


def get_oneday_valuation(day):
    '''
    获取某一天的所有市值数据
    由于返回数量限制,分股票代码 0 3 6 开头三次取数据.
    如何分表呢,将res按股票代码切分为5个res,分别存入5张表中

    '''
    for x in ['0', '3', '6']:

        # get_fundamentals(query(valuation),date)
        qry = query(
            valuation
        ).filter(
            valuation.code.ilike(x + '__________')
        )
        res = get_fundamentals(qry, day)
        res = res.drop(['id'], axis=1)

        # 增加模列
        res['mod'] = res['code'].map(lambda x: int(x[:6]) % 5)

        res0 = res.loc[res['mod'] == 0].drop(['mod'], axis=1)
        res1 = res.loc[res['mod'] == 1].drop(['mod'], axis=1)
        res2 = res.loc[res['mod'] == 2].drop(['mod'], axis=1)
        res3 = res.loc[res['mod'] == 3].drop(['mod'], axis=1)
        res4 = res.loc[res['mod'] == 4].drop(['mod'], axis=1)

        # '''清理老数据'''
        sql0 = "delete from t_valuation_0 where day = '" + \
            day + "' and code like '" + x + "%'"
        sql1 = "delete from t_valuation_1 where day = '" + \
            day + "' and code like '" + x + "%'"
        sql2 = "delete from t_valuation_2 where day = '" + \
            day + "' and code like '" + x + "%'"
        sql3 = "delete from t_valuation_3 where day = '" + \
            day + "' and code like '" + x + "%'"
        sql4 = "delete from t_valuation_4 where day = '" + \
            day + "' and code like '" + x + "%'"
        mdbconn = mysql.connector.connect(
            user='root',
            password='12345678',
            database='jqdata',
            use_unicode=True)
        cursor = mdbconn.cursor()
        cursor.execute(sql0)
        cursor.execute(sql1)
        cursor.execute(sql2)
        cursor.execute(sql3)
        cursor.execute(sql4)
        mdbconn.commit()
        cursor.close()

        '''DataFrame入库'''
        pymysql.install_as_MySQLdb()
        mysqlconnect = create_engine(
            'mysql+mysqldb://root:12345678@localhost:3306/jqdata?charset=utf8')
        res0.to_sql(
            name='t_valuation_0',
            con=mysqlconnect,
            schema='jqdata',
            if_exists='append',
            index=False,
            chunksize=1000)
        res1.to_sql(
            name='t_valuation_1',
            con=mysqlconnect,
            schema='jqdata',
            if_exists='append',
            index=False,
            chunksize=1000)
        res2.to_sql(
            name='t_valuation_2',
            con=mysqlconnect,
            schema='jqdata',
            if_exists='append',
            index=False,
            chunksize=1000)
        res3.to_sql(
            name='t_valuation_3',
            con=mysqlconnect,
            schema='jqdata',
            if_exists='append',
            index=False,
            chunksize=1000)
        res4.to_sql(
            name='t_valuation_4',
            con=mysqlconnect,
            schema='jqdata',
            if_exists='append',
            index=False,
            chunksize=1000)
        print(
            "all " +
            day +
            "valuation data saved in t_valuation_[0,4] success")

    return


jq.auth('18620668927', 'minpeng123')
# 如果传入非交易日,将会获取到之前的最近一个交易日数据,但是删除数据库历史数据删除传入日期,导致后续插入数据失败.
# 使用交易日表 按日期循环取历史
get_oneday_valuation('2019-07-05')
jq.logout()
