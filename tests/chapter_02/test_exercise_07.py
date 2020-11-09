""" Test exercise_07 """
import pytest

from src.chapter_02.exercise_07 import ubbi_dubbi


def test_empty_string():
    """ Verify it works with empty string """
    assert ubbi_dubbi("") == ""


@pytest.mark.parametrize(
    "word, expected",
    [
        ("milk", "mubilk"),
        ("program", "prubogrubam"),
        ("octopus", "uboctubopubus"),
        ("elephant", "ubelubephubant"),
    ],
)
def test_ubbi_dubbi(word, expected):
    """ Verify a word can be converted to Ubbi Dubbi """
    assert ubbi_dubbi(word) == expected
