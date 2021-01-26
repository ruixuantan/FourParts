from fourparts import Interval, Order, MelodicInterval

import pytest


def test_cases():

    return [
        (
            MelodicInterval(Interval.Octave, Order.Static, 1),
            MelodicInterval(Interval.Octave, Order.Static, 1),
        ),
        (
            MelodicInterval(Interval.PerfectFourth, Order.Ascending, 2),
            MelodicInterval(Interval.PerfectFourth, Order.Descending, 2),
        ),
        (
            MelodicInterval(Interval.PerfectFifth, Order.Descending, 3),
            MelodicInterval(Interval.PerfectFifth, Order.Ascending, 3),
        ),
    ]


@pytest.mark.parametrize("melodic_interval, expected", test_cases())
def test_eval(melodic_interval, expected):
    assert melodic_interval.swap_order() == expected
