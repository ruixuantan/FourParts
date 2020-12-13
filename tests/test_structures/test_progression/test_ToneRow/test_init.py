from fourparts import Notes, NoteProgression, ToneRow, ToneRowException

import pytest


def test_cases():
    return [
        (
            [9, 2, 11, 4, 5, 7, 6, 8, 1, 10, 3, 0]
        ),
        (
            [21, 2, 11, 40, 5, 0, 19, 6, 8, 25, 34, 3]
        )
    ]


@pytest.mark.parametrize("note_ints", test_cases())
def test_eval(note_ints):
    progression = []
    for note_int in note_ints:
        progression.append(Notes(note_int))
    note_progression = NoteProgression(progression)

    assert ToneRow(note_progression).tone_row == note_progression


def exception_cases():
    return [
        ([1, 3, 5], pytest.raises(ToneRowException)),
        ([21, 2, 14, 40, 5, 0, 19, 6, 8, 25, 34, 3], pytest.raises(ToneRowException))
    ]


@pytest.mark.parametrize("note_ints, exception", exception_cases())
def test_exceptions(note_ints, exception):
    progression = []
    for note_int in note_ints:
        progression.append(Notes(note_int))
    note_progression = NoteProgression(progression)

    with exception:
        assert ToneRow(note_progression) is not None
