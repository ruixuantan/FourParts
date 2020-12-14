from fourparts import Notes, Interval, Order, MelodicInterval
import pytest


def test_cases():
    return [
        (Notes(0), MelodicInterval(Interval.PerfectFifth, Order.Ascending), Notes(7)),
        (Notes(13), MelodicInterval(Interval.Tritone, Order.Descending), Notes(7)),
        (Notes(0), MelodicInterval(Interval.Semitone, Order.Descending), Notes(11)),
        (Notes(13), MelodicInterval(Interval.Octave, Order.Static), Notes(13)),
    ]


@pytest.mark.parametrize("note, melodic_interval, expected", test_cases())
def test_eval(note, melodic_interval, expected):
    assert note.create_note_with_melodic_interval(melodic_interval) == expected
