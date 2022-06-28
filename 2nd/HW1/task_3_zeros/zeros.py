def zeros(n: int) -> int:
    """
    Returns amount of trailing zeros for n!
    :param n: input integer
    :return: amount of zeros
    """
    power = 1
    result = 0

    while n // (5 ** power) >= 1:
        result += n // (5 ** power)
        power += 1

    return result


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(7) == 1
assert zeros(8) == 1
assert zeros(9) == 1
assert zeros(10) == 2
assert zeros(30) == 7
assert zeros(100) == 24
assert zeros(101) == 24
assert zeros(105) == 25
assert zeros(111) == 26
assert zeros(200) == 49
