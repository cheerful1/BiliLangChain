from fastapi import APIRouter
from pydantic import BaseModel, Field, field_validator
from datetime import date # 年月日，类型， datetime是时分秒这个类型。
from typing import List, Union, Optional

from fastapi import Form,File,UploadFile

import os

app05 = APIRouter()



@app05.post("/file")
async def get_file(file: bytes = File()): # 文件是字节流,接收的是字节流的文件对象
    # 适合小文件上传，这里是上传到文件的内存当中，
    print("file",file)
    return {
        "file": len(file)
    }


@app05.post("/files")
async def get_file(files: List[bytes] = File()): # 文件是字节流,接收的是字节流的文件对象
    # 适合小文件上传，这里是上传到文件的内存当中，
    # print("file",files)
    for file in files:
        print(len(file))

    return {
        "file": len(files)
    }

@app05.post("/uploadFile")
async def get_file(file: UploadFile):
    # 适合小文件上传，这里是上传到文件的内存当中，
    print("file",file)

    # for line in file:
    # 文件操作等

    # 存起来
    path = os.path.join("./imgs",file.filename)

    with open(path, "wb") as f:
        for line in file.file:
            f.write(line)


    return {
        "file": file.filename
    }


@app05.post("/uploadFiles")
async def get_file(files: List[UploadFile]):

    return {
        "file": [file.filename for file in files]
    } 