# closures.py

def outer_func():
    message = 'hi'

    def inner_func():
        print(message)

    return inner_func     # returns function (doesn't call it)


my_func = outer_func()
my_func()                 # => 'Hi'

print(my_func.__name__)


"""
-- a closure is an inner function that remembers and has access to 
   variables in the local scope in which it was created
-- the outer function has finished executing... yet we still have access
"""

def outer_func2(msg):
    message = msg

    def inner_func2():
        print(message)

    return inner_func2    # returns function (doesn't call it)


hi_func2 = outer_func2('Hi')
hello_func2 = outer_func2('Hello')

hi_func2()              # => 'Hi'                                      
hello_func2()           # => 'Hello'

print(my_func.__name__)