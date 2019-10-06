# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(" "))
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


PI = 3.14
radius = get_number()
# Get ABC
crypt = {}
count = 0
while count < 26:
    k = get_word()
    crypt[k] = get_number()
    count += 1
total_degrees = 0

word_to_calculated = get_word()
last_letter = word_to_calculated[0]
for letter in word_to_calculated[1:]:
    if letter in crypt:
        old_deg = crypt[last_letter]
        new_deg = crypt[letter]
        if last_letter == letter:
            pass
        # new letter is higher than old letter swap
        if new_deg < old_deg:
            new_deg, old_deg = old_deg, new_deg
        if new_deg - old_deg <= old_deg - new_deg + 360:
            total_degrees += new_deg - old_deg
        else:
            total_degrees += old_deg - new_deg + 360
one_round = PI * 2 * radius
if total_degrees > 360:
    total_full_round = int(total_degrees/360)
    leftover = total_degrees % 360
else:
    total_full_round = 0
    leftover = total_degrees

total_size = int(total_full_round + (2 * PI * radius) * (leftover/360))
print(total_size)
