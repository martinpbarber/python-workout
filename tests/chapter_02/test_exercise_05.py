""" Test exercise_05 """
import pytest

from src.chapter_02.exercise_05 import pig_latin


def test_empty_string():
    """ Verify it works with empty string """
    assert pig_latin("") == ""


@pytest.mark.parametrize(
    "word, expected",
    [
        ("eat", "eatway"),
        ("air", "airway"),
        ("python", "ythonpay"),
        ("computer", "omputercay"),
    ],
)
def test_pig_latin(word, expected):
    """ Verify a word can be converted to Pig Latin """
    assert pig_latin(word) == expected
