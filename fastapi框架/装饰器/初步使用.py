import time


# def check(fn):
#     def inner():
#         print("登录验证...")
#         fn()
#     return inner
# @check
# def comment():
#     print("发表评论")
#
# comment()

# comment = check(comment)
# comment()



# 统计时间
# 1、定义装饰器
def get_time(fn):
    def inner():
        start_time = time.time()
        fn()
        end_time = time.time()
        print("时间：",end_time - start_time)
    return inner

@get_time
def func():
    for i in range(100000):
        print(i)

func()