from fourparts import Notes
import pytest


def test_cases():
    return [
        ("C", 0),
        ("C#/Db", 1),
        ("D", 2),
        ("D#/Eb", 3),
        ("E", 4),
        ("F", 5),
        ("F#/Gb", 6),
        ("G", 7),
        ("G#/Ab", 8),
        ("A", 9),
        ("A#/Bb", 10),
        ("B", 11),
    ]


@pytest.mark.parametrize("note, expected", test_cases())
def test_eval(note, expected):
    assert Notes.get_note_index(note) == expected


def exception_cases():
    return [("not a note", pytest.raises(KeyError))]


@pytest.mark.parametrize("note, exception", exception_cases())
def test_exception(note, exception):
    with exception:
        assert Notes.get_note_index(note) is not None
