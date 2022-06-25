import json

import mitmproxy.http
from mitmproxy import http, ctx


class Rewrite:
    def response(self, flow: mitmproxy.http.HTTPFlow):
        url="https://stock.xueqiu.com/v5/stock/batch/quote.json?_t"
        if url in flow.request.pretty_url and "x="in flow.request.pretty_url:
            ctx.log.info(f"响应数据:{flow.response.text}")#打印响应数据
            ctx.log.info(str(type(flow.response.text)))#强转成字符串格式
            data=json.loads(flow.response.text)#转成字典格式
            data["data"]["items"][1]["quote"]["name"]="HTDHTDHTDHTDHTD"#mock数据的修改
            data["data"]["items"][1]["quote"]["current"]=9999.99
            data["data"]["items"][1]["quote"]["percent"] = -0.1
            flow.response.text=json.dumps(data)


addons = [
    Rewrite()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    mitmdump(['-p','8080','-s',__file__])

