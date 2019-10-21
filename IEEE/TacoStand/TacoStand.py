from math import floor

N = int(input())

for _ in range(N):
    ing_list = list(map(int, input().split()))
    tortillas = ing_list[0]

    ingredients = ing_list[1:]

    ingredients.sort()

    if ingredients[0] + ingredients[1] > ingredients[2]:
        min_in_tortilla = floor((ingredients[0] + ingredients[1] + ingredients[2]) / 2)
    else:
        min_in_tortilla = ingredients[0] + ingredients[1]

    print(min(min_in_tortilla, tortillas))
