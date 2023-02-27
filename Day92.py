# In this we will be learning about the functool and function caching


import functools
import time


@functools.lru_cache(maxsize=None)
def fun(n):
    time.sleep(5)
    return n * 5


print(fun(2))
print("Printed after 5 seconds")
print(fun(4))
print("Printed after 5 seconds")
print(fun(2))
print("Printed after 5 seconds")