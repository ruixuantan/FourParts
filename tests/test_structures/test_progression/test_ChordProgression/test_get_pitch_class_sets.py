from fourparts import Chord, ChordProgression, PitchClassSet

import pytest


def test_cases():

    return [
        ([Chord(0, 4, 7, 10), Chord(0, 3, 5, 8), Chord(6, 8, 12, 15)],
         [PitchClassSet.create_pitch_class_set(0, 4, 7, 10),
          PitchClassSet.create_pitch_class_set(0, 3, 5, 8),
          PitchClassSet.create_pitch_class_set(6, 8, 12, 15)])
    ]


@pytest.mark.parametrize("chords, expected", test_cases())
def test_eval(chords, expected):
    assert ChordProgression(chords).get_pitch_class_sets() == expected
