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


M = int(input())
mtx = [[0] * M for _ in range(M)]
nums = []

for i in range(M):
    for j in range(M):
        mtx[i][j] = get_number()

sum_diagonal = 0

for i in range(M):
    sum_diagonal += mtx[i][i]

total_sum = 0
for i in range(M):
    total_sum += mtx[i][M - 1 - i]

if total_sum != sum_diagonal:
    nums.append(0)

for i in range(M):
    total_sum = 0
    for j in range(M):
        total_sum += mtx[i][j]
    if total_sum != sum_diagonal:
        nums.append(i + 1)

for j in range(M):
    total_sum = 0
    for i in range(M):
        total_sum += mtx[i][j]
    if total_sum != sum_diagonal:
        nums.append(j * -1 - 1)

nums.sort()
print(len(nums))
for i in range(len(nums)):
    print(nums[i])
