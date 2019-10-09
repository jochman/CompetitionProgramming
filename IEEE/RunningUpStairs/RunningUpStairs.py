import sys

sys.setrecursionlimit(sys.getrecursionlimit() * 100)


def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


input_parser = parser()


def get_word():
    global input_parser
    return next(input_parser)


def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


# Save all of the results instead of calculate them every time
cache = {}


def memoize(f):
    return lambda *args: cache[args] if args in cache else cache.update({args: f(*args)}) or cache[args]


@memoize
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


counter = get_number()
while counter:
    steps = get_number()
    print(fib(steps + 1))
    counter -= 1
