# Python的拆包（Unpacking）是一种将可迭代对象中的元素分配给多个变量的操作，其应用场景广泛且不同数据类型的拆包方式存在显著差异

# 1、多变量赋值
# 返回元组或列表时，可直接拆包到多个变量
def get_data():
    return "Alice", 25, "Engineer"
name, age, job = get_data()
print(name, age, job)

# 2、嵌套结构处理：遍历元组列表或字典时，直接拆包嵌套元素
points = [(1, 2), (3, 4)]
for x, y in points:  # 拆包每个坐标对
    print(x, y)

# 3、字典使用 .items() 拆包键值对：
data = {"name": "Bob", "age": 30}
for key, value in data.items():
    print(key, value)

# 4、函数参数传递
# 动态参数传递：使用 * 和 ** 拆包列表/元组或字典作为位置参数和关键字参数：
def func(a, b, c):
    print(a, b, c)
args = [1, 2, 3]
func(*args)  # 等效于 func(1, 2, 3)


# 不同数据类型的拆包差异

## 1、元组与列表
## 均按位置顺序拆包，变量数量需与元素数量一致（否则报错 ValueError）
## 扩展拆包：使用 * 捕获剩余元素，生成列表
a, *rest = [1, 2, 3, 4]  # a=1, rest=[2,3,4][6,9]

## 2、字典
## 默认拆包键（Keys）：直接拆包字典会得到键而非值：
d = {"a": 1, "b": 2}
k1, k2 = d  # k1="a", k2="b"

## 3、按字符拆包：字符串作为字符序列，拆包后得到单个字符：
s = "hello"
a, b, *c = s  # a='h', b='e', c=['l','l','o']

# 4、集合（Set）
# 无序性影响：因集合无序，拆包顺序不固定，需谨慎使用。

