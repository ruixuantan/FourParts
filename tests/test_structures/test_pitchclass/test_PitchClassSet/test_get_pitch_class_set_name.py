from fourparts import PitchClassSet

import pytest


def test_cases():

    test_cases = [
        ([], "Empty Set"),
        ([0], "Unison"),
        ([0, 5], "Perfect 4th"),
        ([0, 4, 7], "Major"), 
        ([0, 3, 6, 9], "Diminished 7th"),
        ([0, 1, 2], "Not Named")
    ]

    return test_cases


@pytest.mark.parametrize("pitches, name", test_cases())
def test_eval(pitches, name):
    assert name == PitchClassSet.get_pitch_class_set_name(pitches)
