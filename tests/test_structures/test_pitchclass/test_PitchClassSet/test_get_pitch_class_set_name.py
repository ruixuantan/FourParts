from fourparts import PitchClassSet
from fourparts.structures.pitchclass.PitchClassSetMap import (
    PITCH_CLASS_SET_MAP,
    NOT_NAMED,
)

import pytest


def test_empty_set():
    assert PITCH_CLASS_SET_MAP[0][()] == PitchClassSet.get_pitch_class_set_name()


def test_unison():
    assert PITCH_CLASS_SET_MAP[1][(0,)] == PitchClassSet.get_pitch_class_set_name(0)


def test_cases():

    return [
        ((0, 5), PITCH_CLASS_SET_MAP[2][(0, 5)]),
        ((0, 4, 7), PITCH_CLASS_SET_MAP[3][(0, 4, 7)]),
        ((0, 3, 6, 9), PITCH_CLASS_SET_MAP[4][(0, 3, 6, 9)]),
        ((0, 1, 2), NOT_NAMED),
    ]


@pytest.mark.parametrize("pitches, name", test_cases())
def test_eval(pitches, name):
    assert name == PitchClassSet.get_pitch_class_set_name(*pitches)
