def check_me(lst, sum_number):
    lst_set = set()
    while lst:
        now = int(lst.pop(0))
        new = sum_number - now
        if new in lst_set:
            return f"{new} {now}" if new < now else f"{now} {new}"
        lst_set.add(now)
    return "!OK"


number_of_tests = int(input())
while number_of_tests > 0:
    sum_number, total = input().split(" ")
    if total == "0":
        print("!OK")
        input()
    else:
        sum_number = int(sum_number)
        lst = input().split(" ")
        print(check_me(lst, sum_number))
    number_of_tests -= 1
