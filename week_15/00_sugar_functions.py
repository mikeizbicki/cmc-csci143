'''
Functions are objects that implement the __callable__ method.
'''

def example_function():
    print('example_function')

example_function()


class ExampleFunction:
    def __call__(self):
        print('ExampleFunction')

example_function2 = ExampleFunction()
example_function2()
