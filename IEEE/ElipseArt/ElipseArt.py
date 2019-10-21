from typing import List

from numpy.ma import sqrt


class Ellipse:
    def __init__(self, x1, y1, x2, y2, r):
        self.x1 = x1
        self.y2 = y2
        self.y1 = y1
        self.x2 = x2
        self.r = r


def in_ellipse(ellipse: Ellipse, x, y):
    term1 = x - ellipse.x1
    term1 = term1 * term1
    term2 = y - ellipse.y1
    term2 = term2 * term2
    term3 = x - ellipse.x2
    term3 = term3 * term3
    term4 = y - ellipse.y2
    term4 = term4 * term4
    return sqrt(term1 + term2) + sqrt(term3 + term4) <= ellipse.r


def compute():
    def check_ellipses():
        for ellipse in ellipse_list:
            if in_ellipse(ellipse, x, y):
                return 1
        return 0

    cell_count = 0
    for x in range(-499, 499, 10):
        for y in range(-499, 499, 10):
            cell_count += check_ellipses()

    print(f"{round(100 - cell_count-2)}%")


ellipse_list: List[Ellipse] = []

tests = int(input())
while tests:
    number_of_ellipses = int(input())
    while number_of_ellipses:
        ellipse_list.append(Ellipse(*map(int, input().split())))
        number_of_ellipses -= 1
    compute()
    tests -= 1
