try:
    # 1 / 0
    print(name)
except ZeroDivisionError as ze:
    print("异常",ze)
except NameError as ne:
    print("名称错误",ne)
else:
    print("123")
