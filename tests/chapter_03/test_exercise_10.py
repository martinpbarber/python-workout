""" Test exercise_10 """
import pytest

from src.chapter_03.exercise_10 import mysum


def test_no_parameters():
    """ Verify it works with no arguments """
    assert mysum() == None


@pytest.mark.parametrize(
    "arguments, expected",
    [
        ([0], 0),
        ([1, 1], 2),
        ([1, 2, 3], 6),
        ([1, 2, 3, 4], 10),
        ([[1, 2, 3], [4, 5, 6]], [1, 2, 3, 4, 5, 6]),
        (["abc", "def"], "abcdef"),
    ],
)
def test_mysum_numbers(arguments, expected):
    """ Verify it works with various length argument lists """
    assert mysum(*arguments) == expected
