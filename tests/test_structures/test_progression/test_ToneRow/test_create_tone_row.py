from fourparts import NoteProgression, ToneRow
from tests.test_structures.test_progression.test_ToneRow.tone_row_samples import TONEROW

import pytest


def test_cases():
    return [
        ([9, 2, 11, 4, 5, 7, 6, 8, 1, 10, 3, 0], TONEROW),
        ([21, 2, 23, 4, 5, 7, 6, 32, 1, 10, 39, 60], TONEROW),
    ]


@pytest.mark.parametrize("note_ints, expected", test_cases())
def test_eval(note_ints, expected):
    assert (
        ToneRow.create_tone_row(NoteProgression.create_note_progression(note_ints))
        == expected
    )
