import random
import string
import json


# 生成随机数
def build_random(randlen):
    chars = string.ascii_letters + string.digits
    return ''.join([random.choice(chars)
                    for i in range(randlen)])  # 得出的结果中字符会有重复的
    # return ''.join(random.sample(chars, 15))#得出的结果中字符不会有重复的


# 格式化数据
def data_to_json(data):
    # pandas.DataFrame.to_json 转成 JSON string  split格式化
    myjson = json.loads(data.to_json(orient='split'))
    # ensure_ascii 是 false，这些字符会原样输出 so, 就不会用 ASCII 编码，中文就可以正常显示了
    newjson = json.dumps(dice_json(myjson), ensure_ascii=False)
    return newjson


def mess(data):
    mes = {
        "request_id": "4dd8872076fd11e9842ad00dd36710041557916591635050",
        "code": 0,
        "msg": None,
        "data": data
    }
    return mes

# 遍历字典类型的json_string文件所有的key对应的value，并返回一个dice
def dice_json(dic_json):
    dicts = {'fields': 0, 'items': 0}
    if isinstance(dic_json, dict):  # 判断是否是字典类型isinstance 返回True false
        for key in dic_json:
            # print("****key--：%s value--: %s"%(key,dic_json[key]))
            if key == 'columns':
                dicts['fields'] = dic_json[key]
            if key == 'data':
                dicts['items'] = dic_json[key]
            else:
                continue

    return mess(dicts)
