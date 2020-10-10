from fourparts import (
    MelodicInterval, Bass, Tenor, Alto, Soprano,
    VoicingInterval, TenorSoprano, AltoSoprano, BassSoprano
)
from fourparts.exceptions.NoteOrderException import NoteOrderException

import pytest


def test_cases():
    return [
        (Tenor(9), Soprano(10), MelodicInterval.Semitone),
        (Alto(20), Soprano(20), MelodicInterval.Octave),
        (Bass(30), Soprano(50), MelodicInterval.MinorSixth)
    ]


@pytest.mark.parametrize("bottom_voice, top_voice, interval", test_cases())
def test_eval(bottom_voice, top_voice, interval):
    voicing_interval = VoicingInterval.create_voicing_interval(bottom_voice, top_voice)
    assert voicing_interval.melodic_interval == interval


def exception_cases():
    return [
        (Tenor(9), Soprano(1), pytest.raises(NoteOrderException))
    ]


@pytest.mark.parametrize("top_voice, bottom_voice, exception", exception_cases())
def test_exception(top_voice, bottom_voice, exception):
    with exception:
        assert VoicingInterval.create_voicing_interval(top_voice, bottom_voice) is not None
