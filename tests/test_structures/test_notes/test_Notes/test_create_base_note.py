from fourparts import Notes
import pytest


def test_cases():
    return [
        (0, Notes(0)),
        (13, Notes(1)),
        (29, Notes(5)),
        (60, Notes(0))
    ]


@pytest.mark.parametrize("note_int, expected", test_cases())
def test_eval(note_int, expected):
    assert Notes.create_base_note(note_int) == expected


def exception_cases():
    return [
        (-1, pytest.raises(ValueError))
    ]


@pytest.mark.parametrize("note_int, exception", exception_cases())
def test_exception(note_int, exception):
    with exception:
        assert Notes.create_base_note(note_int) is not None
