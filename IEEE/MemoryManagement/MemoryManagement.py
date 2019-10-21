import math


def calc_page(address, s):
    return math.floor(address / s)


test_cases = int(input())
while test_cases:
    pages, size, number = map(int, input().split())

    page_calls = []
    j = 0
    while j < number:
        address = int(input())
        page_calls.append(calc_page(address, size))
        j += 1

    # FIFO
    queue = []
    fifo_counter = 0
    for page in page_calls:
        if page not in queue:
            if len(queue) == pages:
                if queue:
                    del queue[0]
                queue.append(page)
                fifo_counter += 1
            else:
                queue.append(page)

    # LRU
    lru_list = []
    lru_counter = 0
    for page in page_calls:
        if len(lru_list) and lru_list[0] != page or not len(lru_list):
            if page in lru_list:
                k = lru_list.index(page)
                list0, list1, list2 = [page], lru_list[0: k], lru_list[k + 1: len(lru_list)]
                lru_list = (list0 + list1) + list2
            else:
                if len(lru_list) == pages:
                    lru_list.insert(0, page)
                    lru_list.pop()
                    lru_counter += 1
                else:
                    lru_list.insert(0, page)
    if fifo_counter > lru_counter:
        print(f'yes {fifo_counter} {lru_counter}')
    else:
        print(f'no {fifo_counter} {lru_counter}')
    test_cases -= 1
