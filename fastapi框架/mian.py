import uvicorn
from fastapi import FastAPI
from apps.app03 import app03
from apps.app04 import app04
from apps.app05 import app05
from apps.app06 import app06
from apps.app07 import app07
from fastapi.staticfiles import StaticFiles
app = FastAPI()


app.include_router(app03,tags=["03 请求体数据"])
app.include_router(app04,tags=["form表单数据"])
app.include_router(app05,tags=["文件上传"])

app.mount("/static", StaticFiles(directory="statics"), name="static")


app.include_router(app06,tags=["06 Request对象"])

app.include_router(app07,tags=["07 响应参数"])

if __name__ == '__main__':
    uvicorn.run("mian:app",port=8080,reload=True)