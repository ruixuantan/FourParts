from fourparts import Chord, PitchClassSet

import pytest


def test_cases():
    test_cases = [
        (Chord(0, 1, 2, 3), PitchClassSet.create_pitch_class_set(0, 1, 2, 3)),
        (Chord(1, 8, 12, 25), PitchClassSet.create_pitch_class_set(1, 8, 12, 25))
    ]

    return test_cases


@pytest.mark.parametrize("chord, expected", test_cases())
def test_eval(chord, expected):
    generated_result = chord.get_pitch_class_set()
    assert generated_result == expected
