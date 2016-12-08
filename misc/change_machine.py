def change(money, coins):
    """
    @type money: int
    @type coins: list[int]
    @rtype: int
    >>> change(4, [1,2])
    3
    >>> change(10, [5,2,3])
    4
    >>> change(11, [5,7])
    0
    """
    if money == 0:
        return 1
    elif money < 0:
        return 0
    else:
        res = 0
        i = 0
        while i < len(coins):
            res += change(money - coins[i], coins[i:])
            i += 1
        return res
