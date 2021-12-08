from mitmproxy import http

def request(flow: http.HTTPFlow):
    with open("C:/Users/MIANENE/Desktop/test.json") as f:
        if flow.request.pretty_url == "https://www.baidu.com/":
            flow.response = http.HTTPResponse.mark(
                200,
                # b"Hello world!!!",
                f.read(),    # 读取本地文件
                {"Content-Type": "text/html"}
            )

def response(flow: http.HTTPFlow):
    if flow.request.pretty_url == "https://www.baidu.com/":
        flow.response.text = "xxxxxx"