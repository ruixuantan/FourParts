from fourparts import Bass, Soprano, MelodicInterval, VoicingInterval, PreProcessor
import pandas as pd
import pytest


def test_cases():
    test_cases = [
        (
            pd.read_csv('samples/chorale_G_2parts.csv'),
            [
                VoicingInterval(Bass(43),
                                Soprano(67),
                                MelodicInterval.Octave),
                VoicingInterval(Bass(55),
                                Soprano(67),
                                MelodicInterval.Octave),
                VoicingInterval(Bass(52),
                                Soprano(67),
                                MelodicInterval.MinorThird),
                VoicingInterval(Bass(50),
                                Soprano(74),
                                MelodicInterval.Octave),
                VoicingInterval(Bass(52),
                                Soprano(71),
                                MelodicInterval.PerfectFifth),
                VoicingInterval(Bass(42),
                                Soprano(71),
                                MelodicInterval.PerfectFourth),
                VoicingInterval(Bass(42),
                                Soprano(69),
                                MelodicInterval.MinorThird),
                VoicingInterval(Bass(43),
                                Soprano(67),
                                MelodicInterval.Octave),
                VoicingInterval(Bass(47),
                                Soprano(67),
                                MelodicInterval.MinorSixth),
                VoicingInterval(Bass(45),
                                Soprano(67),
                                MelodicInterval.MinorSeventh),
                VoicingInterval(Bass(45),
                                Soprano(69),
                                MelodicInterval.Octave),
                VoicingInterval(Bass(43),
                                Soprano(71),
                                MelodicInterval.MajorThird),
                VoicingInterval(Bass(50),
                                Soprano(69),
                                MelodicInterval.PerfectFifth)
            ]
        )
    ]

    return test_cases


@pytest.mark.parametrize("df, expected", test_cases())
def test_eval(df, expected):
    assert PreProcessor(2).get_progression(df) == expected
