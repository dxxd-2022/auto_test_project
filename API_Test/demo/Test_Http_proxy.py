import requests


def test_post_httpbin():
    #可以通过挂上代理来排除错误 例如：分别postman与python脚本发送请求，比对结果，有可能是传参格式不一样
    proxies={'http':'http://localhost:8888','https':'https://localhost:8888'}
    url="https://httpbin.testing-studio.com/post"
    data={
    "name":"zhangsan",
    "age":22
}
    ret=requests.post(url=url,data=data,proxies=proxies,verify=False)
    print(ret.text)
