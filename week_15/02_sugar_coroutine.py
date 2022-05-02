'''
Explanation of [PEP342 - Coroutine via Enhanced Generators](https://peps.python.org/pep-0342/)
(2005)
'''


def coroutine():
    '''
    This function demonstrates how yield can be used to send and receive data.

    >>> c = coroutine()
    >>> c.send(None)
    0
    >>> c.send('hello')
    value= hello
    1
    >>> c.send('world')
    value= world
    2
    '''
    i = 0
    while True:
        value = yield i
        i += 1
        print("value=",value)


def maximum():
    '''
    A coroutine with slightly more complicated internal state.
    It returns the maximum value that has been sent to it.

    >>> m = maximum()
    >>> m.send(None)
    >>> m.send(5)
    5
    >>> m.send(15)
    15
    >>> m.send(3)
    15
    >>> m.send(16)
    16
    >>> m.send(6)
    16
    '''
    maxi = None
    while True:
        n = yield maxi
        maxi = n if maxi is None or n > maxi else maxi
