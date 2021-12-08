from mitmproxy import http

def request(flow: http.HTTPFlow):
    if flow.request.pretty_url == "https://www.baidu.com/":
        flow.response = http.HTTPResponse.mark(
            200,
            b"Hello world!!!",
            {"Content-Type": "text/html"}
        )
