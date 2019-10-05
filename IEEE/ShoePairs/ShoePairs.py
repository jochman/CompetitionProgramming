lst = list()
count = 0
loops = int(input())
while loops > 0:
    entry = tuple(input().split(" "))
    try:
        if entry[1] == "L":
            new_entry = (entry[0], "R")
        else:
            new_entry = (entry[0], "L")
        lst.index(new_entry)
        lst.remove(new_entry)
        count += 1
    except ValueError:
        lst.append(entry)
    loops -= 1

print(count)
