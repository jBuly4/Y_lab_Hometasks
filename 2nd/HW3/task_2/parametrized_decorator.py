import time


def decorator(call_count: int, start_sleep_time: int, factor: int, border_sleep_time: int):
    """
    Decorator for call_count times execution of function.
    :param call_count: number of executions
    :param start_sleep_time: initial time to sleep
    :param factor: factor for time to sleep increasing
    :param border_sleep_time: max value of time to sleep
    :return: decorated function
    """

    def outer_wrapper(func):
        def inner_wrapper(*args, **kwargs):
            count = 1
            time_to_sleep = start_sleep_time
            while count <= call_count:
                result = func(*args, **kwargs)
                print(
                    f'Запуск номер {count}. Ожидание: {time_to_sleep} секунд. Результат декорируемой функций = '
                    f'{result}.'
                    )
                time.sleep(time_to_sleep)
                time_to_sleep *= 2 ** factor
                if time_to_sleep > border_sleep_time:
                    time_to_sleep = border_sleep_time
                count += 1

        return inner_wrapper
    return outer_wrapper


@decorator(6, 2, 1, 20)
def some_func():
    pass


if __name__ == "__main__":
    some_func()
