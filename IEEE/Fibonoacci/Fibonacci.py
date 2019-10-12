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


fib_array = [1, 1]


def fib(n):
    if n <= len(fib_array):
        return fib_array[n - 1]
    else:
        temp_fib = fib(n - 1) + fib(n - 2)
        fib_array.append(temp_fib)
        return temp_fib


counter = get_number()
while counter:
    nth = get_number()
    print(fib(nth + 1) % 10)
    counter -= 1
