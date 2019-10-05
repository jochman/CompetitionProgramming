# a simple parser for python. use get_number() and get_word() to read
import sys


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


total_bits = get_number()
count = total_bits + 1
arr = [0] * total_bits
# send list of 0s
i = 0
query = "Q "
for bit in arr:
    query += f"{bit} "
print(query)
correct_guesses = get_number()
while count > 0:
    i = 0
    while i < total_bits:
        arr[i] = 1
        query = "Q "
        for bit in arr:
            query += f"{bit} "
        print(query)
        new_correct_guesses = get_number()
        if new_correct_guesses < correct_guesses:
            arr[i] = 0
        elif new_correct_guesses == total_bits:
            query = "A "
            for bit in arr:
                query += f"{bit} "
            print(query)
            sys.exit(0)
        else:
            correct_guesses = new_correct_guesses

        i, count = i + 1, count - 1
