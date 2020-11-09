""" Test exercise_06 """
import pytest

from src.chapter_02.exercise_06 import pl_sentence


def test_empty_string():
    """ Verify it works with empty string """
    assert pl_sentence("") == ""


def test_pl_sentence():
    """ Verify all words in a string are translated to Pig Latin """
    english_sentence = "this is a test translation"
    expected = "histay isway away esttay ranslationtay"

    pig_latin_sentence = pl_sentence(english_sentence)
    assert pig_latin_sentence == expected
