'''
Explanation of [PEP255 - Simple Generators](https://peps.python.org/pep-0255/)
(2001)
'''

def factorial_list(n):
    '''
    Compute the factorial of every number from 1 to n.
    Uses O(n) time and O(n) space.
    '''
    ret = []
    x = 1
    for i in range(1, n+1):
        x *= i
        ret.append(x)
    return ret


'''
>>> for i in factorial_list(10):
>>>     print("i=",i)
'''


def factorial_generator(n):
    '''
    Compute the factorial of every number from 1 to n.
    Uses O(n) time and O(1) space.
    '''
    x = 1
    for i in range(1, n+1):
        x *= i
        yield x

'''
>>> for i in factorial_generator(10):
>>>     print("i=",i)
'''


class Factorial:
    '''
    This is a "desugared" version of the factorial_generator function.
    '''
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return FactorialIter(self.n)


class FactorialIter:
    def __init__(self, n):
        # all of the local variables in the generator function
        # are defined as class member variables here
        self.n = n
        self.ret = 1
        self.i = 0

    def __next__(self):
        '''
        The purpose of this function is to return the "next" factorial number in our sequence.
        The factorial number corresponding to position self.i
        '''
        if self.n <= self.i:
            raise StopIteration
        else:
            self.i += 1
            self.ret *= self.i
            return self.ret


'''
>>> for i in Factorial(10):
>>>     print("i=",i)
>>> 
>>> # the for loop above desugars into the following
>>> tmp = Factorial(10).__iter__()
>>> while True:
>>>     try:
>>>         i = tmp.__next__()
>>>         print("i=",i)
>>>     except StopIteration:
>>>         break
'''
