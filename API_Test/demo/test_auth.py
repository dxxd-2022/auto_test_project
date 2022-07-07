import requests
from requests.auth import HTTPBasicAuth
#有认证条件的需要加上认证信息才可以，否则会报401
def test_auth():
    url='https://httpbin.testing-studio.com/basic-auth/curry/123'
    r=requests.get(url=url,auth=HTTPBasicAuth('curry',123))
    print(r.text)