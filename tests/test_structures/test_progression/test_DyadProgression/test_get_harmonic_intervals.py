from fourparts import Dyad, DyadProgression, MelodicInterval

import pytest


def test_cases():
    return [
        (
            [Dyad(60, 65)],
            [MelodicInterval.PerfectFourth]
        ),
        (
            [Dyad(60, 65), Dyad(62, 65)],
            [MelodicInterval.PerfectFourth, MelodicInterval.MinorThird]
        ),
        (
            [Dyad(10, 20), Dyad(17, 18), Dyad(15, 23)],
            [MelodicInterval.MinorSeventh, MelodicInterval.Semitone, MelodicInterval.MinorSixth]
        )
    ]


@pytest.mark.parametrize("dyad_progression, results", test_cases())
def test_eval(dyad_progression, results):
    generated_results = DyadProgression(dyad_progression).get_harmonic_intervals()
    assert generated_results == results
