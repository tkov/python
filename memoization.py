# memoization.py
import time

# NAIVE
# def expensive_func(num):
#     print("Computing {} ...".format(num))
#     time.sleep(1)
#     result = num * num
#     return result

# USING CACHE
ef_cache = {}  # dictionary
def expensive_func(num):
    if num in ef_cache:
        return ef_cache[num]
    print("Computing {} ...".format(num))
    time.sleep(1)
    result = num * num
    ef_cache[num] = result
    return result

result = expensive_func(4)
print(result)

result = expensive_func(10)
print(result)

result = expensive_func(4)
print(result)

result = expensive_func(10)
print(result)

print(ef_cache)