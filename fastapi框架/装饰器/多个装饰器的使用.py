# 多个装饰器装饰不同的功能。
def check1(fn1):
    def inner1():
        print("登录验证1")
        fn1()
    return inner1


def check2(fn2):
     def inner2():
         print("登录验证2")
         fn2()
     return inner2


@check1 # 这个顺序决定了执行函数的顺序
@check2
def comment():
    print("发表评论")

comment()