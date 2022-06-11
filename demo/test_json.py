import json
#json.dump()把数据类型转换成字符串并存储在文件中
info=[{'name':'curry','age':'33'},
      {'name':'jams','age':'36'}]
print('读取json文件')
json.dump(info,open('datas_test/json_dump.json','w'))


