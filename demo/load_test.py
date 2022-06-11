#json.dump()把数据类型转换成字符串并存储在文件中

import json

json_obj=json.load(open('datas_test/json_load.json','r',encoding="utf-8"))
print(json_obj)
print(type(json_obj))
print(json_obj[1]['title'])