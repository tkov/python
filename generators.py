import random

# Generators

def square_numbers(nums):
    for i in nums:
        yield (i * i)

my_nums = square_numbers([1,2,3,4,5])

my_nums = [x * x for x in [1,2,3,4,5]] # list comprehension
my_nums = (x * x for x in [1,2,3,4,5]) # generator comprehension

print(next(my_nums))
