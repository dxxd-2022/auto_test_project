import requests

#企业微信接口测试实战1
def test_requests():
    corpid = "wwcdd93b018cee1764"
    corpsecret = "f-NvZDfruu9epcUa-rYILIdZEGKvNbJfZjthMZaTtB4"#f代表字符串中可以使用变量，可以用{}加入变量
    url=f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"#获取token
    r=requests.get(url)
    #r.json 代表把结果转换成json
    #编码时，尽量不要使用[]取字典中的数据，尽量使用get;如果元素不存在，python的[]会报异常，而get不会
    token=r.json().get('access_token')#获取企业微信access_token
    r=requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={token}")#获取标签列表
    print(r.json())
    #直接断言外部状态码并不明显，因为前后端很少用外部状态码做联调
    assert r.json().get('errcode')==0
#     datas={
#    "tagname": "UI",
#    "tagid": 12
# }
    # json=? 代表传入数据体
    # data=? 达标传入其他格式数据体
    # r=requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={token}",json=datas)#创建标签接口
    # print(r.json())

    # r=requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={token}&tagid={12}")
    # print(r.json())
