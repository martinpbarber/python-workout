""" Test exercise_08 """
import pytest

from src.chapter_02.exercise_08 import strsort


def test_empty_string():
    """ Verify it works with empty string """
    assert strsort("") == ""


@pytest.mark.parametrize(
    "word, expected",
    [
        ("cba", "abc"),
    ],
)
def test_strsort(word, expected):
    """ Verify a word can be converted to Ubbi Dubbi """
    assert strsort(word) == expected
