import requests


# def test_env():
#     data = {
#         "method": "get",
#         "url": "http://testing-studio:9999/base64_demo.txt",
#         "headers": None
#     }
#     data["url"]=str(data["url"]).replace("testing-studio","127.0.0.1")
#     re=requests.request(method=data['method'],url=data["url"])
#     print(re.text)

class Env:
    def env_replace(self,data:dict):
        data["url"]=str(data["url"]).replace("testing-studio","127.0.0.1")#请求之前实现替换域名
        res=requests.request(method=data["method"],url=data["url"],headers=data["headers"])#二次封装requests
        return res