""" Test exercise_02 """
import pytest

from src.chapter_01.exercise_02 import mysum


def test_no_numbers():
    """ Verify itworks with no arguements """
    assert mysum() == 0


@pytest.mark.parametrize(
    "numbers, expected",
    [([0], 0), ([1, 1], 2), ([1, 2, 3], 6), ([1, 2, 3, 4], 10)],
)
def test_mysum(numbers, expected):
    """ Verify it works with various length arguement lists """
    assert mysum(*numbers) == expected
