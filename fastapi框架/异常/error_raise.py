import logging
logging.basicConfig(
    filename='error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


logger = logging.getLogger(__name__) # 自动为每个模块创建独立的日志记录器

try:
    # 可能出错的代码
    result = 10 / 0
except ZeroDivisionError as e:
    # 记录异常到日志（三种方式）

    # 方式1：使用logger.error() + exc_info=True（推荐）
    logger.error("发生除零错误: %s", e, exc_info=True)



def process_data(data):
    try:
        print(f"处理 {data}")
        if not data.isdigit():
            raise ValueError("非数字数据")
        return int(data) * 2

    except ValueError as ve:
        print(f"值错误: {ve}")
        return None
    finally:
        print(f"完成 {data} 的处理")


# 测试
print(process_data("123"))  # 正常数字
print(process_data("abc"))  # 无效数据