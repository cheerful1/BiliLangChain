import asyncio
from utils import async_timed

@async_timed
async def main():
    print('hello')
    await asyncio.sleep(2)
    print('goodbye')

if __name__ == '__main__':
    #　创建一个协程，并不是直接运行ｍａｉｎ函数，并且这个协程这里不会自己运行的。
    asyncio.run(main())


#　需要放在事件循环中
#  有一個协程队列，存储所有需要执行的协程\
queue = [cor1,cor2]
while True:
    cor = queue.pop()
    result = await cor
