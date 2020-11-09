""" Test exercise_09 """

from src.chapter_03.exercise_09 import firstlast


def test_empty_string():
    """ Verify it works with empty string """
    assert firstlast("") == ""


def test_empty_list():
    """ Verify it works with empty list """
    assert firstlast([]) == []


def test_empty_tuple():
    """ Verify it works with empty tuple """
    assert firstlast(()) == ()


def test_string():
    """ Verify the first and last characters are returned as a string """
    assert firstlast("abc") == "ac"


def test_list():
    """ Verify the first and last list items are returned as a list """
    assert firstlast([1, 2, 3, 4]) == [1, 4]


def test_tuple():
    """ Verify the first and last list items are returned as a list """
    assert firstlast((1, 2, 3, 4)) == (1, 4)
