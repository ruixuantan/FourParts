from fourparts import Notes, Interval, Order, MelodicInterval
import pytest


def test_cases():
    return [
        (
            Notes(0),
            MelodicInterval(Interval.PerfectFifth, Order.Ascending, 0),
            Notes(7),
        ),
        (Notes(13), MelodicInterval(Interval.Tritone, Order.Descending, 0), Notes(7)),
        (Notes(0), MelodicInterval(Interval.Semitone, Order.Descending, 0), Notes(11)),
        (Notes(13), MelodicInterval(Interval.Octave, Order.Static, 0), Notes(13)),
        (
            Notes(10),
            MelodicInterval(Interval.MinorSixth, Order.Ascending, 2),
            Notes(42),
        ),
    ]


@pytest.mark.parametrize("note, melodic_interval, expected", test_cases())
def test_eval(note, melodic_interval, expected):
    assert note.create_note_with_melodic_interval(melodic_interval) == expected
