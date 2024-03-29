import math


def find_primes(number):
    primes = []
    for num in range(1, int(number / 2) + 1):
        # prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes


def find_goldbach(number, primes):
    run_to = len(primes)
    first_number = primes[-1]
    i = run_to - 2
    while i > 0:
        j = 0
        while j < i:
            if first_number + primes[i] + primes[j] == number:
                return f"{first_number} {primes[i]} {primes[j]}"
            j += 1
        i -= 1
    return "counterexample"


def get_number():
    return int(input())


def main():
    number = get_number()
    print(find_goldbach(number, find_primes(number)))


if __name__ == "__main__":
    main()
