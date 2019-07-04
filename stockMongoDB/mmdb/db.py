#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-04 15:13
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : db.py
# @Software: PyCharm

from pymongo import *  # MongoDB的连接库
import json
import os

# 构建一个默认的MongoDB对象置于项目运行的内存当中，避免频繁
# 的创建MongoDB对象
config_file =  os.getcwd()+'/config/db_config.json' # 上面创建的那个json文件的路径
try:
    with open(config_file) as f:
        l = f.read()
        a = json.loads(l)
        db = a['default']  # 默认访问的数据库，上文说过
    uri = 'mongodb://localhost:27017/'
    fields = db.keys()
    uri += '/?connectTimeoutMS=2000'
    if 'replicaset' in fields:
        uri += ';replicaSet=%s' % db['replicaset']
    # if 'dbauth' in fields:
    #     uri += ';authSource=%s' % db['dbauth']
    print('db-uri:', uri)
    connection = MongoClient(uri)
    if 'dbname' in fields:
        mongodb = connection[db['dbname']]
    else:
        mongodb = None
except Exception:
    raise Exception('connection MongoDB raise a error')


class MongoDB:
    """数据库对象"""
    connection_count = 0
    # 当你在程序中，需要访问另一个数据库，那你就需要再临时创建一个连接对象了
    # 为了避免连续访问相同的数据库对象，设置location、connection
    # 两个类属性，保留最近一次访问的对象
    location = None
    connection = None
    db_name = None

    @classmethod
    def db_connection(cls, location, db_name=None):
        """
        连接到数据库
        :param db_name:
        :param location:
        :return:
        """
        try:
            if location == cls.location and cls.connection is not None:
                # 这个连接对象已经存在
                if db_name is not None:
                    return cls.connection[db_name]
                else:
                    # 正常情况下，cls.connection不为空的时候，cls.db_name
                    # 也不为空
                    return cls.connection[cls.db_name]
            else:
                with open(config_file) as cf:
                    buffer = cf.read()
                    jn = json.loads(buffer)
                    db_ = jn[location]
                fields = db_.keys()
                uri = 'mongodb://'
                # if 'username' in fields and 'password' in fields:
                #     uri += '{username}:{password}@'.format(username=db_['username'],
                #                                            password=db_['password'])
                # ip是必须的
                uri += db_['host']
                # if 'port' in fields:
                #     uri += ':%s' % db_['port']
                uri += '/?connectTimeoutMS=2000'
                if 'replicaset' in fields:
                    uri += ';replicaSet=%s' % db_['replicaset']
                # if 'dbauth' in fields:
                #     uri += ';authSource=%s' % db_['dbauth']

                print('new db-uri:', uri)
                connection = MongoClient(uri)
                tn = db_name if db_name is not None else db_['dbname']
                cls.location = location
                cls.connection = connection
                cls.db_name = tn
                return connection[tn]
        except Exception:
            raise Exception('connection MongoDB raise a error')