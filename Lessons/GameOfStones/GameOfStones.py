import numpy as np

answers = []
number_of_tests = int(input())
while number_of_tests:
    sl = int(input())
    total_sum = np.sum(list(map(int, input().split()[:sl])))
    if total_sum % 2:
        print('Zack')
    else:
        print('Sam')
    number_of_tests -= 1