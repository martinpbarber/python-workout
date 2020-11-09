""" Test exercise_03 """
import pytest

from src.chapter_01.exercise_03 import run_timing


class Input:  # pylint: disable=too-few-public-methods
    """
    Test class used to mock the Python input function
    """

    def __init__(self, time_in_minutes=None):
        if time_in_minutes is None:
            self.time_in_minutes = []
        else:
            self.time_in_minutes = time_in_minutes
        self.count = 0

    def __call__(self, prompt):
        if prompt == "Enter 10 km run time: ":
            if self.count == len(self.time_in_minutes):
                run_time = ""
            else:
                run_time = self.time_in_minutes[self.count]
                self.count += 1
        else:
            assert False, f"'{prompt}'"

        return run_time


@pytest.mark.parametrize(
    "run_times, expected",
    [
        ([1], 1),
        ([1, 2], 1.5),
        ([1, 2, 3], 2),
        ([1, 2, 3, 4], 2.5),
        ([1.11111, 2.22222], 1.67),
        ([1, 3.33333], 2.17),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 5),
        ([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9], 5.5),
        ([1.123456789, 10.123456789], 5.62),
    ],
)
def test_run_timing(monkeypatch, run_times, expected):
    """ Verify average of run times is calculated properly """

    input_patch = Input(run_times)
    monkeypatch.setattr("builtins.input", input_patch)
    average = run_timing()

    assert average == expected


def test_run_timing_with_no_inputs(monkeypatch):
    """ Verify average is zero with no inputs """

    input_patch = Input()
    monkeypatch.setattr("builtins.input", input_patch)
    average = run_timing()

    assert average == 0
