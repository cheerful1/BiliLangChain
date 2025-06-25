
# # 定义一个类，实现__call__方法
# class Check(object):
#     def __call__(self,*args,**kwargs):
#         print("我是call方法")
#
# c = Check()
# c()  # call 方法就是，对象可以像函数一样调用call方法。

# 定义类装饰器
class Check(object):
    def __init__(self,fn):
        self.__fn=fn
    def __call__(self,*args,**kwargs):
        print("登录")
        self.__fn()

# 被装饰的函数
@Check  # comment = Check(comment)
def comment():
    print("发表评论")

comment() # 变成实例对象，使用call方法，像函数一样执行call方法里的内容，然后再执行自己里面的代码。