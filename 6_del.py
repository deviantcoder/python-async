def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class PlugException(Exception):
    pass


def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            # print('* Plug Exception *')
            break
        else:
            print('........', message)

    return 'Returned from subgen()'

@coroutine
def delegator(g):
    result = yield from g
    print(result)

@coroutine
def delegator2(g):
    while True:
        try:
            data = yield
            g.send(data)
        except PlugException as e:
            g.throw(e)
