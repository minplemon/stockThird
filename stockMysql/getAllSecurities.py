#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-08 14:12
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : getAllSecurities.py
# @Software: PyCharm

import sys
import pandas as pd
import jqdatasdk as jq
import mysql.connector
import pymysql
from sqlalchemy import create_engine


def get_all_securities():
    '''获取全部股票信息'''
    res = jq.get_all_securities(types=['stock'], date=None)
    '''删除type字段'''
    res = res.drop(['type'], axis=1)

    '''清表'''
    mdbconn = mysql.connector.connect(
        user='root',
        password='12345678',
        database='jqdata',
        use_unicode=True)
    cursor = mdbconn.cursor()
    cursor.execute('truncate table t_all_securities')
    mdbconn.commit()
    cursor.close()
    # print('truncate table t_all_securities success')
    '''DataFrame入库'''
    pymysql.install_as_MySQLdb()
    mysqlconnect = create_engine(
        'mysql+mysqldb://root:12345678@localhost:3306/jqdata?charset=utf8')
    res.to_sql(
        name='t_all_securities',
        con=mysqlconnect,
        schema='jqdata',
        if_exists='append',
        index=True,
        index_label='security',
        chunksize=1000)
    print('all securities saved in t_all_securities success')
    return


def main():
    jq.auth('18620668927', 'minpeng123')
    get_all_securities()
    jq.logout()


if __name__ == "__main__":
    sys.exit(main())
