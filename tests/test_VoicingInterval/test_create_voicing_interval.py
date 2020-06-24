from fourparts import *

import pytest


def test_cases():
    test_cases = [
        (Tenor(9), Soprano(10), MelodicInterval.Semitone, 'TenorSoprano'),
        (Bass(30), Soprano(50), MelodicInterval.MinorSixth, 'BassSoprano')
    ]

    return test_cases


@pytest.mark.parametrize("top_voice, bottom_voice, interval, actual_voicing_interval", test_cases())
def test_eval(bottom_voice, top_voice, interval, actual_voicing_interval):
    voicing_interval = VoicingInterval.create_voicing_interval(bottom_voice, top_voice)
    
    assert voicing_interval.interval == interval and \
           voicing_interval.__class__.__name__ == actual_voicing_interval


def exception_cases():
    exception_cases = [
        (Tenor(9), Soprano(1), pytest.raises(Exception))
    ]

    return exception_cases


@pytest.mark.parametrize("top_voice, bottom_voice, exception", exception_cases())
def test_eval(top_voice, bottom_voice, exception):
    with exception:
       assert VoicingInterval.create_voicing_interval(top_voice, bottom_voice) is not None
