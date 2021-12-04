"""
An array of sequences...
"""

"""
container sequences: can hold items of different types
	-- list
	-- tuple
	-- collections.deque

flat sequences: hold items of one type
	-- str
	-- bytes
	-- bytearray
	-- memoryview
	-- array.array

"""

"""
classes from collections.abc

Container          Sequence          MutableSequence
__contains__       __getitem__		 __setitem__
				   __contains__		 __delitem__
Iterable		   __iter__			 insert
__iter__		   __reversed__	     append
				   index			 reverse
Sized			   count	     	 extend
__len__								 pop
									 remove
   									 __iadd__
"""


# insert examples for classes in collections.abc



"""
List comprehensions
"""

symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
	codes.append(ord(symbol))

codes

# using a listcomp
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
codes

# listcomp vs map/filter

symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
beyond_ascii

# [...symbols] creates an array of each character of the initial string
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))


"""
Cartesian Product
"""

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]
tshirts


"""
Generator expressions
"""

symbols = '$¢£¥€¤'
tuple(ord(symbol) for symbol in symbols)
# => (36, 162, 163, 165, 8364, 164)
import array
array.array('I', (ord(symbol) for symbol in symbols))


"""
Tuples!
"""
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates # tuple unpacking

b = 1; a =2
b, a = a, b # swapping values using tuple unpacking

# another example of tuple unpacking is prefixing an argument with a star
# when calling a function

divmod(20,8) # => (2,4)
t = (20, 8)
divmod(*t)   # => (2,4)
quotient, remainder = divmod(*t)

# another example:
# os.path.split() function builds a tuple

import os
_, filename = os.path.split('/home/this/that/there/irsa.pub')
filename	# => 'idrsa.pub'



# using * to grab excess items
a, b, *rest = range(5)
a, b, rest		# => (0, 1, [2, 3, 4])



"""
list.sort and the sorted built-in function
"""

# both take two optional args: 'key' and 'reverse'


fruits = ['grape', 'raspberry', 'apple', 'banana']
sorted(fruits)