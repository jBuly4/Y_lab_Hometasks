cache = {}


def logger(input_func) -> dict:
    """
    Create caching logs of input function using.
    :param input_func: function for caching
    :return: dictionary with cache
    """
    global cache

    def wrapper(args):  # not starred because we know that we have 1 argument
        if args in cache.keys():
            return f'Here is cached value --> {args}:{cache[args]}'
        cache[args] = input_func(args)

        return f'Cached value --> {args}:{cache[args]}'

    return wrapper


@logger
def multiplier(number: int) -> int:
    return number * 2


if __name__ == "__main__":
    print(multiplier(2))
    print(multiplier(2))
    print(multiplier(4))
    print(multiplier(4))
    print(cache)
