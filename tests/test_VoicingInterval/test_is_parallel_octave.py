from fourparts import *

import pytest


def test_cases():
    test_cases = [
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
                Bass(10),
                Soprano(22),
                MelodicInterval.Octave
            ),
            True
        )
    ]

    return test_cases


@pytest.mark.parametrize("vc_1, vc_2, result", test_cases())
def test_eval(vc_1, vc_2, result):
    assert vc_1.is_parallel_octave(vc_2) == result


def exception_cases():
    exception_cases = [
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

    return exception_cases


@pytest.mark.parametrize("vc_1, vc_2, exception", exception_cases())
def test_eval(vc_1, vc_2, exception):
    with exception:
       assert vc_1.is_parallel_octave(vc_2) is not None
