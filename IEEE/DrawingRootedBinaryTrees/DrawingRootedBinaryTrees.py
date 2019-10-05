import sys
import numpy as np
number_of_tests = int(input())
while number_of_tests > 0:
    input()
    total_sum = np.sum([int(x) for x in input().split()])
    if total_sum % 2:
        print('Zack')
    else:
        print('Sam')
    number_of_tests -= 1
sys.exit(0)
