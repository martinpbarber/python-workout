""" Test exercise_01 """

from src.chapter_01.exercise_01 import guessing_game

# Set the number to guess
NUMBER_TO_GUESS = 50


class Input:  # pylint: disable=too-few-public-methods
    """
    Test class used to mock the Python input function
    """

    def __init__(self, guess):
        self.guess = guess

    def __call__(self, prompt):
        if prompt == "Guess the number I'm thinking of between 0 and 100: ":
            pass
        elif prompt == "Guess is lower than number, try again: ":
            self.guess = self.guess + 1
        elif prompt == "Guess is higher than number, try again: ":
            self.guess = self.guess - 1
        else:
            assert False, f"'{prompt}'"

        return self.guess


def test_guessing_game_guess_0(monkeypatch):
    """ Verify that we can guess starting at zero """

    input_patch = Input(0)
    monkeypatch.setattr("builtins.input", input_patch)
    monkeypatch.setattr("random.randint", lambda min, max: NUMBER_TO_GUESS)
    number = guessing_game()

    assert NUMBER_TO_GUESS == number


def test_guessing_game_guess_100(monkeypatch):
    """ Verify that we can guess starting at 100 """

    input_patch = Input(100)
    monkeypatch.setattr("builtins.input", input_patch)
    monkeypatch.setattr("random.randint", lambda min, max: NUMBER_TO_GUESS)
    number = guessing_game()

    assert NUMBER_TO_GUESS == number
