def log(fn):  # fn = sum_num
    # def inner(a,b):  # inner函数也就是fn。所以这里需要加上参数
    #     fn(a,b)
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        return result  # 如果这个值要被返回的，那么在这个函数内部返回结果
    return inner  # 如果加上装饰器之后，传进来的sum_num函数，就是其中的inner函数，如果下面获取的返回值就是inner的返回值。

@log
def sum_num(a,b):
    result =  a + b
    print(result)
    return result

# 没加装饰器的情况，打印出来是3
# def sum_num(a,b):
#     result =  a + b
#     print(result)
#     return result

result = sum_num(1,2)
print(result)