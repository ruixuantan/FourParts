from fourparts import Notes, NoteProgression, MelodicInterval

import pytest


def test_cases():
    return [
        (
            [Notes(60), Notes(72)],
            [MelodicInterval.Octave]
        ),
        (
            [Notes(60), Notes(65)],
            [MelodicInterval.PerfectFourth]
        ),
        (
            [Notes(50), Notes(52), Notes(44), Notes(70)],
            [MelodicInterval.Tone, MelodicInterval.MinorSixth, MelodicInterval.Tone]
        ),
    ]


@pytest.mark.parametrize("notes, expected", test_cases())
def test_eval(notes, expected):
    progression = NoteProgression(notes)
    assert progression.get_intervals() == expected
