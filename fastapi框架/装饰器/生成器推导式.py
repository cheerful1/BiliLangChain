# 列表推导式

data = [x for x in range(100)]
# print(data)
# 如果仅仅需要前面10个数据
# 使用生成器限制

# data就是一个生成器，可以通过next方法来取出
data  = (x for x in range(100))
# print(next(data))

for i in data:
    print(i)