fib_arr = [1, 2]


def set_first_sixty():
    i = 2
    while i < 60:
        fib_arr.append((fib_arr[i - 1] + fib_arr[i - 2]) % 10)
        i += 1


counter = int(input())
# There's a pattern in the first 60 numbers
set_first_sixty()
while counter:
    calc = int(input())
    print(fib_arr[(calc - 1) % 60])
    counter -= 1
