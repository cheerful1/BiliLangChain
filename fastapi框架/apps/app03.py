from fastapi import APIRouter
from pydantic import BaseModel, Field, field_validator
from datetime import date # 年月日，类型， datetime是时分秒这个类型。
from typing import List, Union, Optional

app03 = APIRouter()

class User(BaseModel): # BaseModel
    # name: str = "root" # 默认值
    name:str = Field(pattern="^a")  # 可以使用正则匹配
    age: int = Field(default=0,gt=0,lt=100) # 对输入的年龄做限制。
    birthday: Union[date,None] = None
    friends: List[int]
    description: Optional[str] = None

    @field_validator("name") # 限制对某一个字段的校验，
    def name_must_alpha(cls,value):
        assert value.isalpha(),'name must be alpha'
        return value

# 发过来的数据需要校验
@app03.post("/data")
async def data(user:User): # 这里传进来的数据限定了User这个类型
    print(user,type(user))
    print(user.dict)
    return user


class Data(BaseModel):
    data: List[User]

@app03.put("/data")
async def data2(data:Data):
    return data