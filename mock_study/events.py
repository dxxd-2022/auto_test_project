import mitmproxy
from mitmproxy import ctx


class HTTPEvents:
    """"""
    def requestheaders(self, flow: mitmproxy.http.HTTPFlow):
        """
        HTTP request headers were successfully read. At this point, the body is empty.
        """
        ctx.log("requestheaders: flow")

    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
        The full HTTP request has been read.

        Note: If request streaming is active, this event fires after the entire body has been streamed.
        HTTP trailers, if present, have not been transmitted to the server yet and can still be modified.
        Enabling streaming may cause unexpected event sequences: For example, `response` may now occur
        before `request` because the server replied with "413 Payload Too Large" during upload.
        """
        ctx.log("ffffffff")

    def responseheaders(self, flow: mitmproxy.http.HTTPFlow):
        """
        HTTP response headers were successfully read. At this point, the body is empty.
        """
        ctx.log(f"responseheaders: flow")

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
        The full HTTP response has been read.

        Note: If response streaming is active, this event fires after the entire body has been streamed.
        HTTP trailers, if present, have not been transmitted to the client yet and can still be modified.
        """
        ctx.log("response: flow")

    def error(self, flow: mitmproxy.http.HTTPFlow):
        """
        An HTTP error has occurred, e.g. invalid server responses, or
        interrupted connections. This is distinct from a valid server HTTP
        error response, which is simply a response with an HTTP error code.

        Every flow will receive either an error or an response event, but not both.
        """
        ctx.log("error:flow")
addons = [
    HTTPEvents()
]


if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    mitmdump(['-p','8080','-s',__file__])
