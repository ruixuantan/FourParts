from fourparts import Interval, Order, MelodicInterval

import pytest


def test_cases():

    return [
        (
            MelodicInterval(Interval.Octave, Order.Static),
            MelodicInterval(Interval.Octave, Order.Static)
        ),
        (
            MelodicInterval(Interval.PerfectFourth, Order.Ascending),
            MelodicInterval(Interval.PerfectFourth, Order.Descending)
        ),
        (
            MelodicInterval(Interval.PerfectFifth, Order.Descending),
            MelodicInterval(Interval.PerfectFifth, Order.Ascending)
        )
    ]


@pytest.mark.parametrize("melodic_interval, expected", test_cases())
def test_eval(melodic_interval, expected):
    assert melodic_interval.swap_order() == expected
