import requests

files={"file":open('file','rb')}
url="上传文件接口"
def test_up_file():
    re=requests.post(url=url,files=files)