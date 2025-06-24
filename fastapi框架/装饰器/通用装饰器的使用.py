# 使用装饰器装饰带有参数的函数

import logging
logging.basicConfig(
    filename='error.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


logger = logging.getLogger(__name__) # # 自动为每个模块创建独立的日志记录器
# 定义装饰器
def log(fn):  # fn = sum_num
    # def inner(a,b):  # inner函数也就是fn。所以这里需要加上参数
    #     fn(a,b)
    def inner(*args, **kwargs):
        logger.info("XXX模块开始")
        fn(*args, **kwargs)
        logger.info(f"函数 {fn.__name__} 执行成功")
        logger.info("XXX模块结束")
    return inner

@log
def sum_num(a,b):
    result =  a + b
    print(result)

sum_num(1,2)