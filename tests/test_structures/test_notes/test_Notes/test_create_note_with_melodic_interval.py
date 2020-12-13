from fourparts import Notes, MelodicInterval
import pytest


def test_cases():
    return [
        (Notes(0), MelodicInterval.PerfectFifth, True, Notes(7)),
        (Notes(13), MelodicInterval.Tritone, False, Notes(7)),
        (Notes(0), MelodicInterval.Semitone, False, Notes(11)),
    ]


@pytest.mark.parametrize("note, interval, is_ascending, expected", test_cases())
def test_eval(note, interval, is_ascending, expected):
    assert note.create_note_with_melodic_interval(interval, is_ascending) == expected
