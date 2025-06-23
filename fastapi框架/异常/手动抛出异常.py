def set_age(age):
    if age < 0:
        # print("值错误")
        raise ValueError("值错误")
    else:
        print(age)

try:
    set_age(-18)
except ValueError as e:
    print(e)

