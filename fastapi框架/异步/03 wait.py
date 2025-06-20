import asyncio
from utils import async_timed


async def greet(name,delay):
    await asyncio.sleep(delay)
    return f"Hello {name}"

# wait for
@async_timed
async def main():
    try:
        # wait for 超时了就不会再继续运行下去
        result = await  asyncio.wait_for(greet("张三",2),timeout = 3)
        print(result)
    except asyncio.TimeoutError:
        print("超时了！")


# wait

if __name__ == '__main__':
    asyncio.run(main())