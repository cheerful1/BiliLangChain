# try:
#     value = 8 / 4
#     print(value)
# except:
#     print('error')
# else: # try里面的代码没有发生异常，则运行下面这段代码
#     print('no error')
# finally:
#     print('finally')
import traceback

try:
    value = 8/0
    print(value)
except:
    info = traceback.format_exc()
    print(info) # 使用字符串来保存。