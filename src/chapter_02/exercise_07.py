""" exercise_07 """

from .exercise_05 import is_empty_string


def ubbi_dubbi(english_word):
    """ Convert a word to ubbi_dubbi """
    if is_empty_string(english_word):
        return english_word

    ubbi_dubbi_letters = []
    for letter in english_word:
        if is_vowel(letter):
            # Put "ub" in front of vowels
            letter = f"ub{letter}"
        ubbi_dubbi_letters.append(letter)

    pig_latin_word = "".join(ubbi_dubbi_letters)
    return pig_latin_word


def is_vowel(letter):
    """ Return True if the letter is a vowel """
    return letter in "aeiou"
