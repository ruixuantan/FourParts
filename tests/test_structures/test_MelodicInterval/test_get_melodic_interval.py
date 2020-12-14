from fourparts import Interval

import pytest


def test_cases():

    return [
        (0, 0, Interval.Octave),
        (1, 2, Interval.Semitone),
        (9, 11, Interval.Tone),
        (28, 34, Interval.Tritone),
        (30, 49, Interval.PerfectFifth),
        (10, 3, Interval.PerfectFifth)
    ]


@pytest.mark.parametrize("note_top, note_bottom, expected", test_cases())
def test_eval(note_top, note_bottom, expected):
    assert Interval.get_interval(note_top, note_bottom) == expected
