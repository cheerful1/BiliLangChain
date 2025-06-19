import asyncio
from utils import async_timed

@async_timed
async def main():
    print('hello')
    # 协程必须要等待，也就是必须在前面加上await关键字
    await asyncio.sleep(1)
    # 在协程中，对于那些会发生阻塞的I/O代码，一定不能使用同步的。否则程序就会阻塞在这个同步代码，失去并发性。
    print('goodbye')

if __name__ == '__main__':
    # 创建一个协程对象
    # main（）：这样不是直接执行mian函数，而是创建一个协程
    cor = main()
    asyncio.run(cor)