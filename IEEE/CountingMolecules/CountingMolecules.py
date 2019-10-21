C, H, O = list(map(int, input().split()))

CO2 = ((1 / 4) * (2 * O - H))
H2O = ((1 / 4) * (-4 * C + H + 2 * O))
GLU = ((1 / 24) * (4 * C + H - 2 * O))

if (CO2 % 1 == 0) and (H2O % 1 == 0) and (GLU % 1 == 0) and (CO2 >= 0) and (H2O >= 0) and (GLU >= 0):
    print(f"{int(H2O)} {int(CO2)} {int(GLU)}")
else:
    print("Error")
