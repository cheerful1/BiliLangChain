import contextlib



class Test:
    def t(self):
        print("123")
    def close(self):
        print("资源释放")

with contextlib.closing(Test()) as t1:
    t1.t()