n = int(input())
while n:
    a, b = map(int, input().split())
    d = 0
    while a != b:
        if a > b:
            a = int(a / 2)
        else:
            b = int(b / 2)
        d += 1
    print(d)
    n -= 1
