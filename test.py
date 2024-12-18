def logger(func):
    def wrapper(a, b):
        print(f'{func.__name__} started')
        result = func(a, b)
        print(f'{func.__name__} finished')
        return result

    return wrapper


@logger
def summ(a, b): # summ = logger(summ) = wrapper
    return a + b


# if __name__ == '__main__':
    # ---- 1 ----
    # function = logger(summ)
    # print(function(2, 3))

    # ---- 2 ----
    # print(logger(summ)(2, 3))

    # print(summ(2, 3))


# 1
import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        lis = func(*args, **kwargs)
        finish = time.time()
        # print(f'{func.__name__} executed in: {finish - start:.5f} seconds')
        return lis

    return wrapper


@timing
def make_list(n):
    lis = [i for i in range(n)]
    return lis

l = make_list(10)
print(l)

# 2

def limit_calls(max_calls):
    def decorator(func):
        calls = 0
        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls >= max_calls:
                raise RuntimeError()
            calls += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator


@limit_calls(max_calls=5)
def make_list(n):
    lis = [i for i in range(n)]
    return lis

# l = limit_calls(max_calls=5)(make_list)

for i in range(6):
    try:
        l = make_list(i)
        print(l)
    except RuntimeError:
        print('function was called too many times')
        break
