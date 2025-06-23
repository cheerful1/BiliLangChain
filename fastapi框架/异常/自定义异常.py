class LessZero(Exception):
    def __init__(self, msg,error_code):
        self.msg = msg
        self.error_code = error_code
    def __str__(self):
        return f'{self.error_code}: {self.msg}'



def set_age(age):
    if age < 0:
        # print("值错误")
        raise LessZero("值错误",404)
    else:
        print(age)

try:
    set_age(-18)
except LessZero as e:
    print(e)

