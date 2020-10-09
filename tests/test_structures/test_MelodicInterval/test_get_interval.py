from fourparts import MelodicInterval

import pytest


def test_cases():

    test_cases = [
        (0, 0, MelodicInterval.Octave),
        (1, 2, MelodicInterval.Semitone),
        (9, 11, MelodicInterval.Tone),
        (28, 34, MelodicInterval.Tritone),
        (30, 49, MelodicInterval.PerfectFifth)
    ]

    return test_cases


@pytest.mark.parametrize("note_top, note_bottom, expected", test_cases())
def test_eval(note_top, note_bottom, expected):
    assert MelodicInterval.get_melodic_interval(note_top, note_bottom) == expected


def exception_cases():

    exception_cases = [
        (10, 3, pytest.raises(Exception))
    ]

    return exception_cases


@pytest.mark.parametrize("note_top, note_bottom, exception", exception_cases())
def test_exception(note_top, note_bottom, exception):
    with exception:
        assert MelodicInterval.get_melodic_interval(note_top, note_bottom) is not None
