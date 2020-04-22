import time
from functools import wraps


def time_laps(func=None):
    # save result and time execution

    @wraps(func)
    def wrap_func(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        time_end = time.time() - time_start

        with open('result.txt', 'a') as result_txt:
            result_txt.write(f'The func is {func.__name__!r} in'
                             f'{time_end} secs with result {result}\n')

        return result

    return wrap_func
