from random import randint
from level_sections import Level


while True:
    getting_level = input("1.EASY🔵\n2.NORMAL🟡\n3.HARD🔴\n0.Help📖\nPlease select your difficulty level: 😥: ")

    random_numbers = [(1, 100), (1, 500), (-100, 100)]
    if getting_level == "1" or getting_level.upper() == "EASY":
        Level(a=random_numbers[0][0], b=random_numbers[0][1])
        break
    elif getting_level == "2" or getting_level.upper() == "NORMAL":
        Level(a=random_numbers[1][0], b=random_numbers[1][1])
        break
    elif getting_level == "3" or getting_level.upper() == "HARD":
        Level(a=random_numbers[2][0], b=random_numbers[2][1])
        break
    elif getting_level == "0" or getting_level.upper() == "HELP":
        print(Level.__doc__)
    elif getting_level.upper() == "EXIT" or "quit":
        print('Thank you for playing my game! See you next time. 💖')
        break
    else:
        print('That\'s not a valid number❌, try again.')