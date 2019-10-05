# a simple parser for python. use get_number() and get_word() to read
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


counter = get_number()
height_to_players = dict()
while counter > 0:
    name = get_word()
    height = get_number()
    if height in height_to_players:
        height_to_players[height].append(name)
    else:
        height_to_players[height] = [name]
    counter -= 1

start = 0
for height in sorted(height_to_players):
    group = height_to_players[height]
    end_str = ""
    for name in sorted(group):
        end_str += f"{name} "
    start += 1
    new_start = start + len(group) - 1
    end_str += f'{start} {new_start}'
    start = new_start
    print(end_str)

