from typing import Union

from fastapi import APIRouter


from fastapi import Request

import os

from pydantic import BaseModel,EmailStr

app07 = APIRouter()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str,None] =None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str,None] =None

@app07.post("/user",response_model=UserOut) # 相当于将字段做了一遍过滤，使用response_model来返回
def create_user(user:UserIn):
    # 存到数据库
    return user
