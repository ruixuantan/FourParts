from fourparts import DyadProgression, VoicingInterval, MelodicInterval

import pytest


def test_cases():
    test_cases = [
        (
            [VoicingInterval(60, 65, MelodicInterval.PerfectFourth)],
            [MelodicInterval.PerfectFourth]
        ),
        (
            [
                VoicingInterval(60, 65, MelodicInterval.PerfectFourth),
                VoicingInterval(62, 65, MelodicInterval.MinorThird)
            ],
            [
                MelodicInterval.PerfectFourth,
                MelodicInterval.MinorThird
            ]
        ),
        (
            [
                VoicingInterval(10, 20, MelodicInterval.MinorSeventh),
                VoicingInterval(17, 18, MelodicInterval.Semitone),
                VoicingInterval(15, 23, MelodicInterval.MinorSixth)
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
