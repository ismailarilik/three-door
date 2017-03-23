import random

win = 0
tried = 1000000

for i in range(tried):
    doors = [0, 1, 2]
    car = random.choice(doors)
    chosen = random.choice(doors)
    try:
        others = doors.copy()
        others.remove(car)
        others.remove(chosen)
    except ValueError:
        pass
    if len(others) == 2:
        opened = random.choice(others)
    else:
        opened = others[0]

    othersThanChosen = doors.copy()
    othersThanChosen.remove(chosen)
    othersThanChosen.remove(opened)
    chosenSecondly = othersThanChosen[0]

    if chosenSecondly == car:
        win += 1

print("Win: " + str(win) + "/" + str(tried))
