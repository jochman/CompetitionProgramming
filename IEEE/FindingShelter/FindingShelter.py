N = int(input())
i = 0
list_of_soldiers = []
while i < N:
    list_of_soldiers.append(list(map(float, input().split())))
    i += 1
i = 0
list_of_shelters = []
while i < N:
    list_of_shelters.append(list(map(float, input().split())))
    i += 1

sorted(list_of_soldiers)
sorted(list_of_shelters)