import time
from functools import wraps


def async_timed(func):
      @wraps(func)
      async def wrapper(*args, **kwargs):
          start = time.time()
          try:
              return await func(*args, **kwargs)
          finally:
              end = time.time()
              time_cost = end - start
              print(f"结束执行{func}，耗时{time_cost:.4f}")
      return wrapper
