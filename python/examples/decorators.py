'''
A decorator is a function, or class, that "wraps" another function.

In this example, I use the "@functools.wraps()" decorator because it
    automatically updates some dunder (__) variables to the correct values.
For example:
    Without @functools.wraps the value of "hello.__name__" would be:
        "decorated" not "hello" because the __name__ value is not updated.
'''

import functools

#----------------------------------------
# CLASS decorator example
class ClassDecorator():
    # setup code could go here
    def __init__(self) -> None:
        pass

    # method that is run when you CALL this class (not when an instance is CREATED)
    # putting your decorator here means that it will automatically be called
    #   whenever __call__ is run (when is whenever the method is called)
    #       hello() is the same as hello.__call__()
    def __call__(self, wrappedFunc):
        # wrappedFunc is the function that this wrapper is wrapping ('hello()' below)
        @functools.wraps(wrappedFunc)
        def decorated(*args, **kwargs):
            print('Class decorator - BEFORE')
            wrappedFunc(*args, **kwargs)
            print('Class decorator - AFTER')
        return decorated


@ClassDecorator()
def hello(name: str = 'Class!'):
    print(f'Hello, {name}')


hello()
print(f'Function name: {hello.__name__}')
#----------------------------------------

print('-' * 15)

#****************************************
# FUNCTION decorator example
def FunctionDecorator(wrappedFunc):
    # if you remove this, then the __name__ of hello1() will change from
    # 'hello1' to 'wrapper'
    @functools.wraps(wrappedFunc)
    def wrapper(*args, **kwargs):
        print('Function decorator - BEFORE')
        wrappedFunc(*args, **kwargs)
        print('Function decorator - AFTER')
    return wrapper


@FunctionDecorator
def hello1(name: str = 'Functions!'):
    print(f'Hello, {name}')


hello1()
print(f'Function name: {hello1.__name__}')
#****************************************
