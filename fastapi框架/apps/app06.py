

from fastapi import APIRouter


from fastapi import Request

import os

app06 = APIRouter()


@app06.post("/items")
async def get_item(request: Request):
    print("url信息",request.url)
    print("客户端IP地址",request.client.host)
    print("请求头",request.headers.get("User-Agent"))
    print("cookies",request.cookies)
    return {
        "url信息":request.url,
        "客户端IP地址": request.client.host,
        "请求头":request.headers.get("User-Agent"),
        "cookies":request.cookies
    }