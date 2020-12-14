from fourparts import Notes, NoteProgression, Interval

import pytest


def test_cases():
    return [
        ([Notes(60), Notes(72)], [Interval.Octave]),
        ([Notes(60), Notes(65)], [Interval.PerfectFourth]),
        (
            [Notes(50), Notes(52), Notes(44), Notes(70)],
            [Interval.Tone, Interval.MinorSixth, Interval.Tone],
        ),
    ]


@pytest.mark.parametrize("notes, expected", test_cases())
def test_eval(notes, expected):
    progression = NoteProgression(notes)
    assert progression.get_intervals() == expected
