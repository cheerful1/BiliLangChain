import asyncio
from utils import async_timed

async def greet(name,delay):
    await asyncio.sleep(delay)
    return f"Hello {name}"

# #　用创建任务的方式并发运行
# @async_timed
# async def main():
#     # 并发运行，必须要将协程包装成Task对象，才能够并发执行
#     task1 = asyncio.create_task(greet('xx',1))
#     task2 = asyncio.create_task(greet('yy',2))
#     result1 = await task1
#     print(result1)
#     result2 = await task2
#     print(result2)


async def greet_group(name,delay):
    await asyncio.sleep(delay)
    if name == 'xx':
        raise ValueError("执行错误！")
    return f"Hello {name}"


# # 用gather实现协程的并发
# @async_timed
# async def main():
#     # gather在将所有协程全部都执行完成之后，会按照协程入队的顺序，将协程的返回值存放在results中。
#     results = await  asyncio.gather(
#         greet_group('xx',1),
#         greet('yy', 2),
#         return_exceptions = True # 即使其中的一个协程发生异常，也保证其余的协程正常的工作
#     )
#     print(results)
#
#     # 获取所有的任务
#     tasks = asyncio.all_tasks()
#
#     for task in tasks:
#         # 这里说明，gather中有的任务发生异常了，剩余还没执行完的任务，也不会被取消
#         # print(task.get_name(),task.cancelled())
#         if task.get_name() == 'Task-1':
#             continue

# 4、使用as——completed
@async_timed
async def main():
    aws = [
            greet('xx',1),
            greet('yy', 2)
    ]
    # 可以指定超时时间
    # 如果超过指定的超时时间，那么会抛出TimeoutError异常
    # 剩余的任务不会被取消
    try:
        for coro in asyncio.as_completed(aws,timeout=3): # 没有运行完的会抛出异常，
            result = await coro
            print(result)
    except Exception as e:
        print(e)







if __name__ == '__main__':
    asyncio.run(main())