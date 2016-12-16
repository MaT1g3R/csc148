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


def get_nth_prime(n):
    res = [2]
    i = 3
    while len(res) < n:
        is_prime = True
        for factor in res:
            if i % factor == 0:
                is_prime = False
        if is_prime:
            res.append(i)
        i += 1
    return res[-1]

print(turncatables())
