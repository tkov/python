"""
Functions as objects
"""

# First-class functions

"""
- functions are first-class objects
- they are created at runtime
- they are assigned to a variable or element in a data structure
- they are passed as an argument to a function
- they are returned as the result of a function
"""

# Treating a function like an object

def factorial(n):
	''' returns n!'''
	return 1 if n < 2 else n * factorial(n-1)

factorial(42)
factorial.__doc__ # => 'returns n!'
type(factorial)	  # => <class 'function'>

fact = factorial
fact
# <function factorial at 0x7fe152870310>
factorial
# <function factorial at 0x7fe152870310>
fact(5)
# 120
map(factorial, range(11))
# <map object at 0x7fe150f87520>
list(map(factorial, range(11)))
# [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]


# Higher-order functions
# - a function that takes a function as an argument
#   or returns a function as result is a higher-order function


# sorting a list of words by length
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
sorted(fruits, key=len)
# ['fig', 'apple', ..., 'strawberry']

def reverse(word):
	return word[::-1]

reverse('testing')
sorted(fruits, key=reverse)

# listcomps and genexp does the job of map and filter combined...

list(map(fact, range(6)))
[fact(n) for n in range(6)]

list(map(factorial, filter(lambda n: n % 2, range(6))))
[factorial(n) for n in range(6) if n % 2]


from functools import reduce
from operator import add
reduce(add, range(100))

# equivalent code to reduce
sum(range(100))


"""
Anonymous functions
"""

# the lambda keyword creates an anon function
# the body of lambda must be contain pure expressions
# the body cannot make assignments or use any other Python statement


# an anonymous function that acts as our previous function 'reverse'
sorted(fruits, key=lambda word: word[::-1])


'''
Seven flavors of callable objects
----------------------------------

- use the callable() function to determine callable objects


User-defined: created with def or lambda
Built-in functions: len, time.strftime
Built-in methods: dict.get
Methods: functions defined in the body of a class
Classes: 
	when invoked, a class runs
		-- __new__ method to create an instance
		-- __init__ to initialize it
		-- finally, the instance is returned to the caller
		-- calling a class is like calling a function (because there is no 'new' operator)

Class instances:
	if a class defines a __call__ method, its instances may be invoked as functions

Generator functions: functions or methods that use the 'yield' keyword
	-- when called, generator functions return a generator object

'''

# User-defined callable types

import random

class BingoCage:
	def __init__(self, items):
		self._items = list(items)
		random.shuffle(self._items)

	def pick(self):
		try:
			return self._items.pop()
		except IndexError:
			raise LookupError('pick from empty BingoCage')

	def __call__(self):
		return self.pick()


bingo = BingoCage(range(3))
bingo.pick()	# => 1
bingo()			# => 0
callable(bingo)	# => True


# Function introspection

dir(factorial)

# ex 5-9: listing attribute of functions that don't exist in plain instances

class C: pass 
obj = C()
def func(): pass
sorted(set(dir(func)) - set(dir(obj)))
