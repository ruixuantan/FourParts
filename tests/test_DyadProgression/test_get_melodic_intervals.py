from fourparts import DyadProgression, BassSoprano, MelodicInterval

import pytest


def test_cases():
    test_cases = [
        (
            [BassSoprano(60, 65, MelodicInterval.PerfectFourth)],
            [MelodicInterval.PerfectFourth]
        ),
        (
            [
                BassSoprano(60, 65, MelodicInterval.PerfectFourth),
                BassSoprano(62, 65, MelodicInterval.MinorThird)
            ],
            [
                MelodicInterval.PerfectFourth,
                MelodicInterval.MinorThird
            ]
        ),
        (
            [
                BassSoprano(10, 20, MelodicInterval.MinorSeventh),
                BassSoprano(17, 18, MelodicInterval.Semitone),
                BassSoprano(15, 23, MelodicInterval.MinorSixth)
            ],
            [
                MelodicInterval.MinorSeventh,
                MelodicInterval.Semitone,
                MelodicInterval.MinorSixth
            ]
        )
    ]

    return test_cases


@pytest.mark.parametrize("dyad_progression, results", test_cases())
def test_eval(dyad_progression, results):
    generated_results = DyadProgression(dyad_progression).get_melodic_intervals()
    assert generated_results == results
