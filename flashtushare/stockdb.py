#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-04 11:04
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : stockdb.py
# @Software: PyCharm


import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb2"]
mycol = mydb["sites"]

mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}

x = mycol.insert_one(mydict)
print(x)
print(x)