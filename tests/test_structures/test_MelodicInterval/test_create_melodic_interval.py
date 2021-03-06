from fourparts import Interval, Order, MelodicInterval

import pytest


def test_cases():

    return [
        (70, 70, MelodicInterval(Interval.Octave, Order.Static, 0)),
        (50, 55, MelodicInterval(Interval.PerfectFourth, Order.Ascending, 0)),
        (1, 0, MelodicInterval(Interval.Semitone, Order.Descending, 0)),
        (12, 31, MelodicInterval(Interval.PerfectFifth, Order.Ascending, 1)),
        (60, 30, MelodicInterval(Interval.Tritone, Order.Descending, 2)),
        (20, 35, MelodicInterval(Interval.MinorThird, Order.Ascending, 1)),
    ]


@pytest.mark.parametrize("bottom_note_int, top_note_int, expected", test_cases())
def test_eval(bottom_note_int, top_note_int, expected):
    assert (
        MelodicInterval.create_melodic_interval(bottom_note_int, top_note_int)
        == expected
    )
