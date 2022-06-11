import json
#json.loads(json_string)把字符串转换成json
str='''[{"name":"curry","age":"33"},
      {"name":"jams","age":"36"}]'''
print(type(str))
data=json.loads(str)
print(type(data))
print(data)