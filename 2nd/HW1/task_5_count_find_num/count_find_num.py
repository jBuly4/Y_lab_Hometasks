def lst_multiplication(lst: list) -> int:
    result = 1
    for num in lst:
        result *= num

    return result


def count_find_num(primesL: list, limit: int) -> list:
    """
    Returns list with amount of numbers under limit and max value from that list
    :param primesL: list with prime numbers
    :param limit: limit value
    :return: list with numbers and max value
    """
    # your code here
    # all prime numbers must be inside all generated numbers under limit
    init_num = lst_multiplication(primesL)
    result = []

    if init_num > limit:  # >= doesn't work for test cases
        return result
    else:
        result.append(init_num)

    for prime_num in primesL:
        for num in result:
            current_num = prime_num * num
            while current_num not in result and current_num <= limit:
                result.append(current_num)  # it is possible to iterate and append at the same time
                # https://tutorial.eyehunts.com/python/python-append-to-list-while-iterating-example-code/
                current_num *= current_num * prime_num

    return [len(result), sorted(result, reverse=True)[0]]


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []

primesL = [3, 7]
limit = 21
assert count_find_num(primesL, limit) == [1, 21]

primesL = [2, 3, 7]
limit = 21
assert count_find_num(primesL, limit) == []

primesL = [2, 3, 7]
limit = 42
assert count_find_num(primesL, limit) == [1, 42]
