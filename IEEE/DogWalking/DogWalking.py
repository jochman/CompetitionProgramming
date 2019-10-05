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


test_case = get_number()
while test_case > 0:
    number_of_dogs = get_number()
    num_of_walkers = get_number()
    dogs_list = []
    counter = number_of_dogs
    while counter > 0:
        dogs_list.append(get_number())
        counter -= 1
    dogs_list.sort()

    diff_list = []
    counter = 0
    while counter < number_of_dogs - 1:
        diff_list.append(dogs_list[counter + 1] - dogs_list[counter])
        counter += 1
    diff_list.sort()

    total = dogs_list[-1] - dogs_list[0]
    for i in range(number_of_dogs - num_of_walkers, number_of_dogs-1):
        total -= diff_list[i]
    print(total)
    test_case -= 1
