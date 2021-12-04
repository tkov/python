# www.datacamp.com/community/tutorials/decorators-python
"""
Functions in Python are 'first class citizens'; they can be:
    -- passed as an argument
    -- returned from a function
    -- modified and assigned to a variable
"""

# Assigning Functions to Variables
def plus_one(number):
    return number + 1

add_one = plus_one  # variable = function

print(add_one(5))  # invoke the function by using the variable name instead


# Defining Functions inside other Function
def plus_one(number):
    def add_one(number):
        return number + 1

    result = add_one(number)
    return result

print(plus_one(4))

# Passing Functions as Arguments to other Functions

def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

print(function_call(plus_one))


# Functions returning other Functions
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi

hello = hello_function()
print(hello())


# Nested Functions have access to the Enclosing Function's Variable Scope

def print_message(message):
    # Enclosing function
    def message_sender():
        # Nested function
        print(message)          # message is passed to the enclosing function, yet the nested function can use it

    message_sender()

print_message("Some random message")


# Creating Decorators

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def say_hi():
    return 'hello there!'

decorate = uppercase_decorator(say_hi)
print(decorate())

@ uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())

# Applying Multiple Decorators to a Single FUnction

def split_string(function):
    def wrapper():
        func = function()
        splittled_string = func.split()
        return splitted_string

    return wrapper


