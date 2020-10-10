from fourparts import MelodicInterval, VoicingInterval, Bass, Tenor, Soprano

import pytest


def test_cases():
    return [
        (
            VoicingInterval(
                Tenor(9),
                Soprano(10),
                MelodicInterval.Semitone
            ),
            VoicingInterval(
                Tenor(10),
                Soprano(11),
                MelodicInterval.Semitone
            ),
            False
        ),
        (
            VoicingInterval(
                Bass(9),
                Soprano(16),
                MelodicInterval.PerfectFifth
            ),
            VoicingInterval(
                Bass(9),
                Soprano(16),
                MelodicInterval.PerfectFifth
            ),
            False
        ),
        (
            VoicingInterval(
                Bass(9),
                Soprano(16),
                MelodicInterval.PerfectFifth
            ),
            VoicingInterval(
                Bass(8),
                Soprano(15),
                MelodicInterval.PerfectFifth
            ),
            True
        )
    ]


@pytest.mark.parametrize("vc_1, vc_2, result", test_cases())
def test_eval(vc_1, vc_2, result):
    assert vc_1.is_parallel_fifth(vc_2) == result


def exception_cases():
    return [
        (
            VoicingInterval(
                Bass(9),
                Soprano(16),
                MelodicInterval.PerfectFifth
            ),
            VoicingInterval(
                Tenor(8),
                Soprano(15),
                MelodicInterval.PerfectFifth
            ),
            pytest.raises(Exception)
        ),
        (
            VoicingInterval(
                Bass(9),
                Tenor(16),
                MelodicInterval.PerfectFifth
            ),
            VoicingInterval(
                Bass(8),
                Soprano(15),
                MelodicInterval.PerfectFifth
            ),
            pytest.raises(Exception)
        )
    ]


@pytest.mark.parametrize("vc_1, vc_2, exception", exception_cases())
def test_exception(vc_1, vc_2, exception):
    with exception:
        assert vc_1.is_parallel_fifth(vc_2) is not None
