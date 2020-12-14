from fourparts import Dyad, DyadProgression, Interval

import pytest


def test_cases():
    return [
        (
            [Dyad(60, 65)],
            [Interval.PerfectFourth]
        ),
        (
            [Dyad(60, 65), Dyad(62, 65)],
            [Interval.PerfectFourth, Interval.MinorThird]
        ),
        (
            [Dyad(10, 20), Dyad(17, 18), Dyad(15, 23)],
            [Interval.MinorSeventh, Interval.Semitone, Interval.MinorSixth]
        )
    ]


@pytest.mark.parametrize("dyad_progression, results", test_cases())
def test_eval(dyad_progression, results):
    generated_results = DyadProgression(dyad_progression).get_harmonic_intervals()
    assert generated_results == results
