a, b = map(int, input().split())
if b > a:
    a, b = b, a
counter = 0
if not a or not b:
    print(0)
else:
    spare = a % 2
    a = int(a / 2)
    ans = min(a, b)
    if spare and spare + b - a > 3:
        ans += 1
    print(ans)
