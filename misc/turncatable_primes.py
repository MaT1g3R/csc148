def isprime(n):
    """Returns True if n is prime."""
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


def turncatables():
    i = 10
    turncatable = []
    while len(turncatable) < 11:
        if is_turn(i):
            turncatable.append(i)
        i += 1
    return turncatable


def is_turn(n):
    """
    >>> is_turn(3797)
    True
    """
    for i in range(len(str(n))):
        if not isprime(int(str(n)[i:])) or not isprime(int(str(n)[0:len(str(n)) - i])):
            return False
    return True


def num_divisior(n):
    """
    return the number of divisiors for an int
    @type n: int
    @rtype: int
    >>> num_divisior(14)
    4
    >>> num_divisior(15)
    4
    """
    if n == 1:
        return 1
    else:
        res = 0
        for i in range(n + 1):
            if i == 0:
                continue
            if n % i == 0:
                res += 1
        return res


def same_divisor():
    """
    Find the number of integers 1 < n < 10^7, for which n and n + 1 have the same
    number of positive divisors. For example, 14 has the positive divisors 1, 2,
    7, 14 while 15 has 1, 3, 5, 15.
    """
    res = 0
    for n in range(10**7):
        if num_divisior(n) == num_divisior(n+1):
            res += 1
    return res

print(same_divisor())




