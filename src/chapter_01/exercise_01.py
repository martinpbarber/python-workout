""" exercise_01 """

import random

GUESS_MIN = 0
GUESS_MAX = 100

INITIAL_PROMPT = "Guess the number I'm thinking of between 0 and 100: "
TOO_LOW_PROMPT = "Guess is lower than number, try again: "
TOO_HIGH_PROMPT = "Guess is higher than number, try again: "


def guessing_game():
    """ Guessing game """
    number_to_guess = random.randint(GUESS_MIN, GUESS_MAX)

    guess = input(INITIAL_PROMPT)
    guess = int(guess)
    while guess != number_to_guess:
        if guess < number_to_guess:
            guess = input(TOO_LOW_PROMPT)
        else:
            guess = input(TOO_HIGH_PROMPT)
        guess = int(guess)

    return guess
