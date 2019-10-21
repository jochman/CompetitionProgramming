while True:
    a = input()
    if a == 'END':
        break
    a_int = int(a)
    sz_a = len(a)
    c = 1
    while True:
        if sz_a == a_int:
            print(c)
            break
        else:
            a_int = sz_a
            sz_a = len(str(sz_a))
            c += 1
