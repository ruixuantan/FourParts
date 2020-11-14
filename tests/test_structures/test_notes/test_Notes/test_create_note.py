from fourparts import Notes
import pytest


def test_cases():
    return [
        (0, 0),
        (3, 3),
        (60, 0),
        (68, 8)
    ]


@pytest.mark.parametrize("note_int, expected", test_cases())
def test_eval(note_int, expected):
    assert Notes.create_note(note_int) == Notes.create_note(expected)


def exception_cases():
    return [
        (-1, pytest.raises(ValueError))
    ]


@pytest.mark.parametrize("note_int, exception", exception_cases())
def test_exception(note_int, exception):
    with exception:
        assert Notes.create_note(note_int) is not None
