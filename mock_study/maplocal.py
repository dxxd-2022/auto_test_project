import json

import mitmproxy.http
from mitmproxy import http, ctx


class Maplocal01:
    def request(self, flow: mitmproxy.http.HTTPFlow):
        url="https://stock.xueqiu.com/v5/stock/batch/quote.json?_t"
        #给定监听的url匹配规则
        if url in flow.request.pretty_url and "x="in flow.request.pretty_url:
            #打开本地替换文件
            with open("quote.json",encoding='utf-8')as f:
                #制造响应体
                flow.response=http.HTTPResponse.make(
                    200,
                    f.read()
                )
addons = [
    Maplocal01()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    mitmdump(['-p','8080','-s',__file__])