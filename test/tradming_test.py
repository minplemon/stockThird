#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-21 12:34
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : tradming_test.py
# @Software: PyCharm

import urllib.request
import unittest
import stock.trading as fd


# 测试请求数据
response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))


class Test(unittest.TestCase):

    def set_data(self):
        self.code = '600848'
        self.start = '2015-01-03'
        self.end = '2015-04-07'
        self.year = 2014
        self.quarter = 4

    def test_get_hist_data(self):
        self.set_data()
        print(fd.get_hist_data(self.code, self.start))

    def test_get_tick_data(self):
        self.set_data()
        print(fd.get_tick_data(self.code, self.end))

    def test_get_today_all(self):
        print(fd.get_today_all())

    def test_get_realtime_quotesa(self):
        self.set_data()
        print(fd.get_realtime_quotes(self.code))

    def test_get_h_data(self):
        self.set_data()
        print(fd.get_h_data(self.code, self.start, self.end))

    def test_get_today_ticks(self):
        self.set_data()
        print(fd.get_today_ticks(self.code))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
