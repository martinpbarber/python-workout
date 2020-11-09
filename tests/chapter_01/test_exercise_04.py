""" Test exercise_04 """
import pytest

from src.chapter_01.exercise_04 import hex_output


class Input:  # pylint: disable=too-few-public-methods
    """
    Test class used to mock the Python input function
    """

    def __init__(self, hex_number):
        self.hex_number = hex_number

    def __call__(self, prompt):
        assert prompt == "Enter a hex number to convert: "

        # Input always returns strings
        return str(self.hex_number)


@pytest.mark.parametrize(
    "hexademical, expected",
    [
        (0, 0),
        (50, 80),
        ("A", 10),
        ("B", 11),
        ("C", 12),
        ("D", 13),
        ("E", 14),
        ("F", 15),
        ("1F", 31),
        ("1A2B3C4D5E6F", 28772997619311),
    ],
)
def test_hex_output(monkeypatch, hexademical, expected):
    """ Verify hex to decimal conversion is done properly """

    input_patch = Input(hexademical)
    monkeypatch.setattr("builtins.input", input_patch)
    decimal = hex_output()

    assert decimal == expected
