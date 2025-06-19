from fastapi import APIRouter
from pydantic import BaseModel, Field, field_validator
from datetime import date # 年月日，类型， datetime是时分秒这个类型。
from typing import List, Union, Optional

from fastapi import Form

app04 = APIRouter()

@app04.post("/regin")
async def regin(username: str=Form(),password: str=Form()):
    print(f"username:{username}",f"password:{password}")
    # z注册实现数据库的添加操作
    return {"username":username}