def zero():
    try:
        yield
    except ZeroDivisionError as e:
        print("error",e)

x=1
y=0

with zero():
    x/y