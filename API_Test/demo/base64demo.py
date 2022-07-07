import json

import requests
import base64

def test_base64_demo():
    url = "http://127.0.0.1:9999/base64_demo.txt"
    r = requests.get(url=url)
    print(r.text)
    print("获取二进制内容:",r.content)
    re = json.loads(base64.b64decode(r.content))
    print(re)
class Base64Demo:
    def send(self,data:dict):#data存放请求信息
        res=requests.request(data["method"],data["url"],headers=data["headers"])
        if data["encoding"]=="base64":
            return json.loads(base64.b64decode(res.content))
        #把加密内容发送给第三方服务，第三方服务解密过后返回解密的数据
        elif data["encoding"]=="pri":
            return requests.post("url",data=res.content)#url为第三方解密服务方的地址，data为加密数据


