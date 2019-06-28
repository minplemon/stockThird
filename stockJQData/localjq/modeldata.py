#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-26 18:13
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : modeldata.py
# @Software: PyCharm

import datetime
import pandas as pd
import numpy as np

from stockJQData.localjq.base_model import  BaseModel

from BaseException import MongoIOError, FileError, ExceptionInfo, WarningMessage, SuccessMessage  # 这都是一些关于异常处理的自定义方法，可以先不管，代码中报错的可以先注释掉



class ModelData(object):
    """
    有关公共模型所有的IO（数据库）将通过这个类实现.
    通用的IO方法
    """

    def __init__(self, location=None, dbname=None):
        self.location = location
        self.dbname = dbname
        pass

    # @classmethod
    def field(self, table_name, field_name, filter=None):
        """
        Query the value of a field in the database
        :param filter:
        :param table_name: the database's table name
        :param field_name: the table's field name
        :return: all values in database
        """
        try:
            return BaseModel(table_name, self.location,
                             self.dbname).distinct(field_name, filter)
        except Exception:
            raise MongoIOError('query the field raise a error')

    # @classmethod
    def max(self, table_name, field='_id', **kw):
        """
        找到满足kw条件的field列上的最大值
        :param table_name:
        :param field:
        :param kw:
        :return:
        """
        try:
            if not isinstance(field, str):
                raise TypeError('field must be an instance of str')
            cursor = BaseModel(table_name, self.location,
                               self.dbname).query(sql=kw, field={field: True})
            if cursor.count():
                d = pd.DataFrame(list(cursor))
                m = d.loc[:, [field]].max()[field]
            else:
                m = None
            cursor.close()
            return m
        except Exception as e:
            raise e

    # @classmethod
    def min(self, table_name, field='_id', **kw):
        """
        找到满足kw条件的field列上的最小值
        :param table_name:
        :param field:
        :param kw:
        :return:
        """
        try:
            if not isinstance(field, str):
                raise TypeError('field must be an instance of str')
            cursor = BaseModel(table_name, self.location,
                               self.dbname).query(sql=kw, field={field: True})
            if cursor.count():
                d = pd.DataFrame(list(cursor))
                m = d.loc[:, [field]].min()[field]
            else:
                m = None
            cursor.close()
            return m
        except Exception as e:
            raise e

    # @classmethod
    def insert_data(self, table_name, data):
        """
        一个简易的数据插入接口
        :param table_name:
        :param data:
        :return:
        """
        try:
            if len(data):
                d = data.to_dict(orient='records')
                BaseModel(table_name, self.location,
                          self.dbname).insert_batch(d)
        except Exception:
            raise MongoIOError('Failed with insert data by MongoDB')

    def insert_one(self, table_name, data):
        """
        insert one record
        :param table_name:
        :param data: a dict
        :return:
        """
        try:
            BaseModel(table_name, self.location,
                      self.dbname).insert(data)
        except Exception:
            raise MongoIOError('Failed with insert data by MongoDB')

    def read_one(self, table_name, field=None, **kw):
        """
        有时候只需要读一条数据，没必要使用read_data，
        :param table_name:
        :param field:
        :param kw:
        :return: a dict or None
        """
        try:
            cursor = BaseModel(table_name, self.location,
                               self.dbname).query_one(kw, field)
        except Exception as e:
            ExceptionInfo(e)
        finally:
            return cursor

    # @classmethod
    def read_data(self, table_name, field=None, **kw):
        """
        一个简易的数据读取接口
        :param table_name:
        :param field:
        :param kw:
        :return:
        """
        try:
            cursor = BaseModel(table_name, self.location,
                               self.dbname).query(kw, field)
            data = pd.DataFrame()
            if cursor.count():
                data = pd.DataFrame(list(cursor))
        except Exception as e:
            ExceptionInfo(e)
        finally:
            cursor.close()
            return data

    def aggregate(self, table_name, pipeline):
        """

        :param table_name:
        :param pipeline:
        :return:
        """
        try:
            cursor = BaseModel(table_name, self.location,
                               self.dbname).aggregate(pipeline)
            # data = pd.DataFrame()
            # if cursor.count():
            data = pd.DataFrame(list(cursor))

        except Exception as e:
            ExceptionInfo(e)

        finally:
            cursor.close()
            return data

    # @classmethod
    def update_data(self, table_name, condition, **kw):
        """
        按condition条件更新table_name表数据
        :param table_name:
        :param condition: 形如{‘date':datetime.datetime(2018,1,1)}的一个字典
        :param kw:形如close=0这样的参数组
        :return:
        """
        try:
            r = BaseModel(table_name, self.location,
                          self.dbname).update_batch(condition, kw)
            return r
        except Exception:
            raise MongoIOError('Failed with update by MongoDB')

    # @classmethod
    def remove_data(self, table_name, **kw):
        """
        删除数据
        :param table_name:
        :param kw:
        :return:
        """
        try:
            r = BaseModel(table_name, self.location,
                          self.dbname).remove(kw)
            return r
        except Exception:
            raise MongoIOError('Failed with delete data by MongoDB')