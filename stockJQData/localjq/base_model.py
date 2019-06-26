#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-26 18:12
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : base_model.py
# @Software: PyCharm

import pymongo
from bson import ObjectId

from .db import MongoDB, ASCENDING, DESCENDING, mongodb, connection


class BaseModel(object):
    """
    _id 是 mongo 自带的，必须有这个字段
    其余 __fields__  的固定属性，未来会逐步添加
        classtype 是类名的小写
    """
    __fields__ = [
        '_id',
        # (字段名, 类型)
        # ('classtype', str),
    ]

    def __init__(self, tn=None, location=None, dbname=None):
        name = self.__class__.__name__
        self.tablename = tn.strip() if tn is not None and len(tn) else name.lower()
        if location is None and dbname is None:
            if mongodb is not None:
                self.mc = mongodb[self.tablename]
            else:
                raise Exception('Unable to find available dbname')
        elif location is None and dbname is not None:
            self.mc = connection[dbname][self.tablename]
        else:
            self.location = location
            self.dbname = dbname
            self.mc = MongoDB.db_connection(self.location, self.dbname)[self.tablename]
    def insert(self, *args, **kwargs):
        """
        插入一条数据
        """
        _ = kwargs if len(kwargs) else args[0]
        _['classtype'] = self.tablename
        # 去掉 _id 这个特殊的字段
        if '_id' in _:
            _['_id'] = ObjectId()

        m = self.mc.insert_one(_)
        return m

    def insert_batch(self, *args):
        """
        批量插入数据
        """
        _ = list()
        if len(args) == 1:
            _ = args[0]
            if isinstance(_, list):
                pass
            else:
                _ = [_]

        elif len(args) > 1:
            _ = args

        result = []
        for i in _:
            if '_id' in i:
                i['_id'] = ObjectId()
                # del i['_id']
            i['classtype'] = self.tablename.lower()
        try:
            if len(_):
                result = self.mc.insert_many(_)
        except pymongo.errors.BulkWriteError as e:
            if isinstance(_, list):
                r = _[0]
            else:
                r = _
            #log('insert_batch', self.tablename, r, msg=e.details['writeErrors'])

    def query(self, sql=None, field=None):
        """
        数据查询
        返回 list
        找不到则返回 []
        """
        # _ = kwargs if len(kwargs) else args[0] if len(args) else None
        ds = self.mc.find(sql, projection=field)
        return ds

    def aggregate(self, pipeline, allowDiskUse=True):
        """
        聚合函数
        :param pipeline: list 聚合表达式
        :param allowDiskUse: 运行使用磁盘来处理超过100M的数据
        :return:
        """
        return self.mc.aggregate(pipeline, allowDiskUse=allowDiskUse)

    def query_one(self, sql=None, field=None):
        """
        查找并返回第一个元素
        找不到就返回 None
        """
        # _ = kwargs if len(kwargs) else args[0]
        l = self.mc.find_one(sql, projection=field)
        return l

    def update(self, cond, form):
        """
        """
        self.mc.find_one_and_update(cond, {"$set": form},
                                                        upsert=False)

    def update_batch(self, condition, form):
        """
        批量更新
        :param condition:
        :param form:
        :return:
        """
        return self.mc.update_many(condition, {"set": form})# set前有一个美元符号
        pass

    def distinct(self, field, sql=None):
        return self.query(sql=sql).distinct(field)

    def remove(self, *args, **kwargs):
        _ = kwargs if len(kwargs) else args[0]
        result = self.mc.delete_many(_)