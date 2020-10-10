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
                Bass(10),
                Soprano(22),
                MelodicInterval.Octave
            ),
            VoicingInterval(
                Bass(10),
                Soprano(22),
                MelodicInterval.Octave
            ),
            False
        ),
        (
            VoicingInterval(
                Bass(10),
                Soprano(22),
                MelodicInterval.Octave
            ),
            VoicingInterval(
                Bass(11),
                Soprano(23),
                MelodicInterval.Octave
            ),
            True
        )
    ]


@pytest.mark.parametrize("vc_1, vc_2, result", test_cases())
def test_eval(vc_1, vc_2, result):
    assert vc_1.is_parallel_octave(vc_2) == result


def exception_cases():
    return [
        (
            VoicingInterval(
                Bass(10),
                Soprano(22),
                MelodicInterval.Octave
            ),
            VoicingInterval(
                Tenor(9),
                Soprano(21),
                MelodicInterval.Octave
            ),
            pytest.raises(Exception)
        ),
        (
            VoicingInterval(
                Bass(10),
                Tenor(22),
                MelodicInterval.Octave
            ),
            VoicingInterval(
                Bass(9),
                Soprano(21),
                MelodicInterval.Octave
            ),
            pytest.raises(Exception)
        )
    ]


@pytest.mark.parametrize("vc_1, vc_2, exception", exception_cases())
def test_exception(vc_1, vc_2, exception):
    with exception:
        assert vc_1.is_parallel_octave(vc_2) is not None
