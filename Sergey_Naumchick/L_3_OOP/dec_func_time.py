import time


# Decorating functions saving in file time and result
def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        with open("new_file.txt", "a+") as n_file:
            n_file.write(f"Function {func.__name__} starts at {start}"
                         f"and ends at {end}. Working for {end - start}. RESULT - {args[0]}\n")

    return wrapper
