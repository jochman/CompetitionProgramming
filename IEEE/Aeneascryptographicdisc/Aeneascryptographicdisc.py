import math


def to_polar(r, theta):
    """Gets radian of the spin

    :param r: radius
    :param theta:
    :return: angle in radians
    """
    return r * math.cos(theta), r * math.sin(theta)


def calculate_distance(args):
    """Gets distance from (x1, y1) to (x2, y2)

    :param args:
    :return: distance
    """
    # Unpack values
    x1, y1, x2, y2 = args[0][0], args[0][1], args[1][0], args[1][1]
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


RADIUS = float(input())

COORDINATES = {0: (0, 0)}
for i in range(26):
    # Get letter and position
    letter, theta = input().split()
    # calculate radian
    theta = math.radians(float(theta))
    # calculate polar r*(cos, sin) and apply to the dict
    COORDINATES[letter] = to_polar(RADIUS, theta)

DISTANCES = {}  # Example: {(A, B): 15.2}
for letter1 in COORDINATES.keys():
    """Calculate all distances from any letter to any letter.
    (will decrease future time)
    """
    for letter2 in COORDINATES.keys():
        DISTANCES[letter1, letter2] = \
            calculate_distance((COORDINATES[letter1], COORDINATES[letter2]))

PHRASE_TO_CALCULATE = input().strip().upper()
TOTAL_TRAVEL = 0
PREVIOUS_POSITION = 0
for letter in PHRASE_TO_CALCULATE:
    # add all distances from DISTANCES dict to TOTAL_TRAVEL
    if letter.isalpha():
        TOTAL_TRAVEL += DISTANCES[PREVIOUS_POSITION, letter]
        PREVIOUS_POSITION = letter

print(int(TOTAL_TRAVEL) + 1)
