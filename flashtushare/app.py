from flask import Flask, Response, request
import tushare as ts
import json
from flashtushare.util import data_to_json, build_random
import os ,time


path = os.getcwd() #获取当前工作路径

app = Flask(__name__)

ts.set_token('df6592c4f63cdc4600e6aa1267d3d0f51cdaddcf4c9d554d9b395090')
pro = ts.pro_api()


PATH = '%s/data/%s/%s/%s.csv' #路径，股票，时间，类型
LOCAL_PATH = os.getcwd()

code = '600570'
time = time.strftime('%Y%m%d',time.localtime(time.time()))
datapype = '1min'
_datapype = str.upper(datapype)


ss = PATH%(LOCAL_PATH,code,time,_datapype)
# print(ss)

# filename = os.getcwd()+'/data/600570/20190516.csv'
# filename_zhishu = '/Users/minp/PycharmProjects/flask_v1/data/zhishu/20190516.csv'


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    # path
    # print('%s'%path+'/data/600570/20190516.csv')
    return 'helloword'

hello_world()

@app.route('/realtime_code', methods=['POST'])
def get_bar_code():
    ap = ts.get_apis()
    try:
        data = ts.bar(
            '600570',
            ap,
            start_date='20190516',
            end_date='20190517',
            freq='1min')
        # if os.path.exists(filename):
        #     data.to_csv(filename, mode='a', header=False, encoding='utf-8',na_rep='NA')
        # else:
        #     data.to_csv(filename, encoding='utf-8',na_rep='NA')
    except:
        return None
    content = data_to_json(data)
    resp = Response_headers(content)
    return resp


@app.route('/realtime_quotes', methods=['POST'])
def get_realtime_quotes():
    data = ts.get_realtime_quotes(['sh', 'sz', 'cyb'])
    # if os.path.exists(filename_zhishu):
    #     data.to_csv(filename_zhishu, mode='a',index=False,header=False, encoding='utf-8',na_rep='NA')
    # else:
    #     data.to_csv(filename_zhishu, index=False, encoding='utf-8',na_rep='NA')
    data = data[['code', 'name', 'price', 'volume', 'amount', 'date', 'time']]
    content = data_to_json(data)
    resp = Response_headers(content)
    return resp


# 股票列表
@app.route('/stock_basic', methods=['POST'])
def fun_stock_basic():
    if request.method == 'POST':
        data = pro.stock_basic(
            exchange='',
            list_status='L',
            fields='ts_code,name,area,industry,list_date')
        content = data_to_json(data)
        resp = Response_headers(content)
        return resp
    else:
        content = json.dumps({"error_code": "1001"})
        resp = Response_headers(content)
        return resp


# 股票日期
@app.route('/trade_cal', methods=['POST'])
def fun_trade_cal():
    data = pro.trade_cal(
        exchange='',
        start_date='20180101',
        end_date='20181231')
    return data_to_json(data)


def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.errorhandler(403)
def page_not_found(error):
    content = json.dumps({"error_code": "403"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(404)
def page_not_found(error):
    content = json.dumps({"error_code": "404"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(400)
def page_not_found(error):
    content = json.dumps({"error_code": "400"})
    # resp = Response(content)  
    # resp.headers['Access-Control-Allow-Origin'] = '*'  
    resp = Response_headers(content)
    return resp
    # return "error_code:400"  


@app.errorhandler(410)
def page_not_found(error):
    content = json.dumps({"error_code": "410"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(500)
def page_not_found(error):
    content = json.dumps({"error_code": "500"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(405)
def page_not_found(error):
    content = json.dumps({"error_code": "405"})
    resp = Response_headers(content)
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
