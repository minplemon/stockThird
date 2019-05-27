#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-27 10:47
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : ref_test.py
# @Software: PyCharm

import unittest
from stock import reference as fd


class Test(unittest.TestCase):
    def set_data(self):
        self.code = '600848'
        self.start = '2015-01-03'
        self.end = '2015-04-07'
        self.year = 2014
        self.quarter = 4
        self.top = 60
        self.show_content = True

    def test_profit_data(self):
        self.set_data()
        print(fd.profit_data(top=self.top))

    def test_forecast_data(self):
        self.set_data()
        print(fd.forecast_data(self.year, self.quarter))


if __name__ == '__main__':
    unittest.main()
