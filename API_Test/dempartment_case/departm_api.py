import json

import requests

def test_get_access_token():
    corpid="wwcdd93b018cee1764"
    corpsecret="f-NvZDfruu9epcUa-rYILPIAkZ8kzKtXZ8llhWHzyGo"
    url=f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    r=requests.get(url=url)
    #print(json.dumps(r.json(),indent=2))
    new_token=r.json().get("access_token")
    return new_token
class DepartmApi:
    def get_departm_list(self):
        url=f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={test_get_access_token()}"
        r=requests.get(url=url)
        return r