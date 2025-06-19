from fastapi import FastAPI
import uvicorn
app = FastAPI()
# @app.get("/")
# async def root():
#     return {"Hello": "World"}

@app.get("/") # 这里一定要加上  /
async def home(): # async使用异步
    return {"user": 1001} # 默认转换成json字符串


@app.get("/shop")
async def home(): # async使用异步
    return {"shop": "商品信息"} # 默认转换成json字符串

@app.get(f"/user/{id}")
def get_user(id:int): #这里冒号后面的就是类型说明，如果输入一个 字符串，那么久会强制把id转换成int类型
    return {"user": id}

# 假设在写一个
@ app.get("/user/1")
def get_user(id:int):
    return {"user": "root user"}

from typing import Union





if __name__ == '__main__':
    uvicorn.run("fastapi_quickstart:app",port=8080,reload=True,log_level="debug")