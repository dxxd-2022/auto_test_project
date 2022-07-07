import requests
from jsonpath import jsonpath
url="https://home.testing-studio.com/categories.json"
def test_jsonpath():
    r=requests.get(url=url)
    print(r.json(),'$..name')
    assert jsonpath(r.json(),'$..name')[0]=='提问区'