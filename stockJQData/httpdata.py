#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-31 10:33
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : httpdata.py
# @Software: PyCharm

# coding=utf-8
import requests,json
url="https://dataapi.joinquant.com/apis"
#获取调用凭证
body={
    "method": "get_token",
    "mob": "18620668927",  #mob是申请JQData时所填写的手机号
    "pwd": "minpeng123",  #Password为聚宽官网登录密码，新申请用户默认为手机号后6位
}
response = requests.post(url, data = json.dumps(body))
token=response.text
#调用get_security_info获取单个标的信息
body={
    "method": "get_current_tick",
    "token": '5b6a9ba2b3f273b525667f2c01cd0db28375d8be',
    "code": "502050.XSHG",
}
response = requests.post(url, data = json.dumps(body))
print (response.text)