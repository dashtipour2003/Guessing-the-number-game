from random import randint

def Level(a, b):
    """
    This program has 3 levels:
    The first level is Easy
    The second level is Normal
    The third level is Hard

    By choosing the level number or typing the level name, you can set the difficulty of the game:

    Easy → a random number between 1 and 100
    Normal → a random number between 1 and 250
    Hard → a random number between -100 and 100

    The game will guide you by telling whether the number you guessed is higher or lower.
    """
    RN = randint(a, b)
    do_guess = True
    while do_guess:
        getting_guess = int(input("Enter your guess: "))
        if getting_guess == RN:
            print("Your guess is right!✅")
            do_guess = False
        elif getting_guess < RN:
            print("Your guess is too low, go higher.⬆️")
        elif getting_guess > RN:
            print("Your guess is too high, go lower.⬇️")
