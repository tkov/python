def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)

say_whee()

# why is this useful?

def my_dec2(func):
    print("A")
    func()
    print("B")

    return func

say_whee2 = my_dec2(say_whee)
#say_whee2()