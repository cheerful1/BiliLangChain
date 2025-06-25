def log(fn):  # fn = sum_num
    # def inner(a,b):  # inner函数也就是fn。所以这里需要加上参数
    #     fn(a,b)
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs) # 不定长的参数，不知道参数有几个的时候使用。
        return result
    return inner

@log
def sum_num(a,b):
    result =  a + b
    print(result)
    return result

result = sum_num(1,2)
print(result)