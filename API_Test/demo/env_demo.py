import requests
import yaml
class EnvApi:
    # env={
    #     "default":"dev",
    #     "testing-studio":
    #     {
    #     "dev": "127.0.0.1",
    #     "test": "127.0.0.2"
    #     }
    # }
    env=yaml.safe_load(open("env.yaml"))#通过生成的yaml文件管理环境
    # data = {
    #     "method": "get",
    #     "url": "http://testing-studio:9999/API_Test/base64_demo.txt",
    #     "headers": None,
    # }
    def send(self,data:dict):
        data["url"]=str(data["url"]).replace("http://testing-studio",self.env["testing-studio"][self.env["default"]])#替换url
        r=requests.Request(method=data["method"],url=data["url"],headers=["headers"])
        return r