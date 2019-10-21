counter = int(input())
while counter:
    C, G = map(int, input().split())
    gadgets = [list(map(int, input().split())) for _ in range(G)]
    solutions = [[0] * (C + 1) for _ in range(G + 1)]
    i = 1
    while i < G + 1:
        j = 1
        while j < C + 1:
            new_j = j - gadgets[i - 1][0]
            if new_j < 0:
                solutions[i][j] = solutions[i - 1][j]
                j += 1
                continue
            solutions[i][j] = max(solutions[i - 1][j], gadgets[i - 1][1] + solutions[i - 1][new_j])
            j += 1
        i += 1
    print(solutions[-1][-1])
    counter -= 1
