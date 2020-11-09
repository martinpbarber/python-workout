""" exercise_05 """


def pig_latin(english_word):
    """ Convert a word to Pig Latin """
    if is_empty_string(english_word):
        return english_word

    if word_starts_with_vowel(english_word):
        # Add "way" to the end of the word
        pig_latin_word = english_word + "way"
    else:
        # Move first letter to end of word and add "ay"
        pig_latin_word = english_word[1:] + english_word[0] + "ay"

    return pig_latin_word


def is_empty_string(word):
    """ Return True if the string is empty """
    return not (word and word.strip())


def word_starts_with_vowel(word):
    """ Return True if the sord starts with a vowel """
    return word[0] in "aeiou"
