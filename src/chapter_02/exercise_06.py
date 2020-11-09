""" exercise_06 """
from .exercise_05 import pig_latin, is_empty_string


def pl_sentence(sentence):
    """ Convert a word in a sentence to Pig Latin """
    if is_empty_string(sentence):
        return sentence

    pig_latin_words = []
    for word in sentence.split():
        pig_latin_words.append(pig_latin(word))
    pig_latin_sentence = " ".join(pig_latin_words)

    return pig_latin_sentence
