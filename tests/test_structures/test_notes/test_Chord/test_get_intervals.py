from fourparts import (
    Chord,
    Interval,
    BassTenor,
    BassAlto,
    BassSoprano,
    TenorAlto,
    TenorSoprano,
    AltoSoprano,
)

import pytest


def test_cases():
    test_cases = [
        (
            0,
            1,
            2,
            3,
            Interval.Semitone,
            Interval.Tone,
            Interval.MinorThird,
            Interval.Semitone,
            Interval.Tone,
            Interval.Semitone,
        ),
        (
            30,
            37,
            40,
            45,
            Interval.PerfectFifth,
            Interval.MinorSeventh,
            Interval.MinorThird,
            Interval.MinorThird,
            Interval.MinorSixth,
            Interval.PerfectFourth,
        ),
    ]

    return test_cases


@pytest.mark.parametrize("b, t, a, s, b_t, b_a, b_s, t_a, t_s, a_s", test_cases())
def test_eval(b, t, a, s, b_t, b_a, b_s, t_a, t_s, a_s):
    intervals = Chord(b, t, a, s).get_intervals()

    check_intervals = (
        intervals["BassTenor"].melodic_interval == b_t
        and intervals["BassAlto"].melodic_interval == b_a
        and intervals["BassSoprano"].melodic_interval == b_s
        and intervals["TenorAlto"].melodic_interval == t_a
        and intervals["TenorSoprano"].melodic_interval == t_s
        and intervals["AltoSoprano"].melodic_interval == a_s
    )

    check_names = (
        isinstance(intervals["BassTenor"], BassTenor)
        and isinstance(intervals["BassAlto"], BassAlto)
        and isinstance(intervals["BassSoprano"], BassSoprano)
        and isinstance(intervals["TenorAlto"], TenorAlto)
        and isinstance(intervals["TenorSoprano"], TenorSoprano)
        and isinstance(intervals["AltoSoprano"], AltoSoprano)
    )

    assert check_intervals and check_names
