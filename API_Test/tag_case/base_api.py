import requests

#把常量放在类变量中
class BaseApi:
    CORPID="wwcdd93b018cee1764"
    CORPSECRET="f-NvZDfruu9epcUa-rYILIdZEGKvNbJfZjthMZaTtB4"
    BASE_URL="https://qyapi.weixin.qq.com/cgi-bin/"
    def __init__(self):
        self.token=self.get_token()
    def get_token(self):
        #corpid = "wwcdd93b018cee1764"
        #corpsecret = "f-NvZDfruu9epcUa-rYILIdZEGKvNbJfZjthMZaTtB4"  # f代表字符串中可以使用变量，可以用{}加入变量
        url = self.BASE_URL+f"/gettoken?corpid={self.CORPID}&corpsecret={self.CORPSECRET}"  # 获取token
        r = requests.get(url)
        # r.json 代表把结果转换成json
        # 编码时，尽量不要使用[]取字典中的数据，尽量使用get;如果元素不存在，python的[]会报异常，而get不会
        return r.json().get('access_token')  # 获取企业微信access_token
        # self.token=r.json()['access_token']#获取token方式二 不建议用这种
        # print(self.token)