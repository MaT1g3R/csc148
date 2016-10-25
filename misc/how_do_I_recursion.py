"""
How do i recursion
"""


def fib(n):
    """
    @type n: int
    @rtype: None
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def factorio(n):
    """
    @type n: int
    @rtype: int
    """
    if n == 1:
        return 1
    else:
        return n * factorio(n-1)

print(factorio(3))
