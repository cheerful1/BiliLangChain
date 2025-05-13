# 1、生成列表
squares = [x**2 for x in range(10)]
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 2、大小写转换
uppercase = [s.upper() for s in ["hello", "world"]]
print(uppercase) # ['HELLO', 'WORLD']

lowwercase = [s.lower() for s in ["HELLO"]]
print(lowwercase) # ['hello']

# 3、条件过滤
evens = [x for x in range(10) if x % 2 == 0]
print(evens) # [0, 2, 4, 6, 8]

# 4、复杂表达式与多条件组合
# 过滤负数并加倍非负值
nums = [-5, 0, 2, 4]
result = [x*2 for x in nums if x >= 0]
print(result) # [0, 4, 8]
