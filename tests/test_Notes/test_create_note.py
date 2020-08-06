from fourparts import Notes
import pytest


def test_cases():
    test_cases = [
       (0, Notes('C')),
       (3, Notes('D#/Eb')),
       (60, Notes('C')),
       (68, Notes('G#/Ab'))
    ]

    return test_cases


@pytest.mark.parametrize("note_int, expected", test_cases())
def test_eval(note_int, expected):
    assert Notes.create_note(note_int) == expected


def exception_cases():
    exception_cases = [
        (-1, pytest.raises(ValueError))
    ]

    return exception_cases


@pytest.mark.parametrize("note_int, exception", exception_cases())
def test_exception(note_int, exception):
    with exception:
        assert Notes.create_note(note_int) is not None