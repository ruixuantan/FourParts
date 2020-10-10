from fourparts import MelodicInterval, Bass, Tenor, Alto, Soprano, VoicingInterval

import pytest


def test_cases():
    return [
        (Tenor(9), Soprano(10), MelodicInterval.Semitone, 'TenorSoprano'),
        (Alto(20), Soprano(20), MelodicInterval.Octave, 'AltoSoprano'),
        (Bass(30), Soprano(50), MelodicInterval.MinorSixth, 'BassSoprano')
    ]


@pytest.mark.parametrize("top_voice, bottom_voice, interval, actual_voicing_interval", test_cases())
def test_eval(bottom_voice, top_voice, interval, actual_voicing_interval):
    voicing_interval = VoicingInterval.create_voicing_interval(bottom_voice, top_voice)

    assert voicing_interval.melodic_interval == interval and \
           voicing_interval.__class__.__name__ == actual_voicing_interval


def exception_cases():
    return [
        (Tenor(9), Soprano(1), pytest.raises(Exception))
    ]


@pytest.mark.parametrize("top_voice, bottom_voice, exception", exception_cases())
def test_exception(top_voice, bottom_voice, exception):
    with exception:
        assert VoicingInterval.create_voicing_interval(top_voice, bottom_voice) is not None
