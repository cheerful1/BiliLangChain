import asyncio
from utils import async_timed

async def greet(name,delay):
    await asyncio.sleep(delay)
    return f"Hello {name}"

#　用创建任务的方式并发运行
@async_timed
async def main():
    # 并发运行，必须要将协程包装成Task对象，才能够并发执行
    task1 = asyncio.create_task(greet('xx',1))
    task2 = asyncio.create_task(greet('yy',2))
    result1 = await task1
    print(result1)
    result2 = await task2
    print(result2)


if __name__ == '__main__':
    asyncio.run(main())