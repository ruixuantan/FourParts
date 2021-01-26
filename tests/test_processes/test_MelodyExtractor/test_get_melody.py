from fourparts import MelodyExtractor, Notes, NoteProgression
from tests.samples import (
    PERFECT_CADENCE_CSV,
    TYPEA_PERFECT_CADENCE_CSV,
    CHORALE_F_CSV,
    UNISON_CSV,
)
import pandas as pd
import pytest


def test_cases():
    return [
        (
            pd.read_csv(PERFECT_CADENCE_CSV),
            [Notes(65), Notes(65), Notes(64)],
        ),
        (
            pd.read_csv(TYPEA_PERFECT_CADENCE_CSV),
            [Notes(64), Notes(64), Notes(62)],
        ),
        (
            pd.read_csv(CHORALE_F_CSV),
            [
                Notes(65),
                Notes(65),
                Notes(67),
                Notes(69),
                Notes(67),
                Notes(65),
                Notes(64),
                Notes(61),  # MelodyExtractor cannot differentiate between voices
                Notes(62),
            ],
        ),
        (
            pd.read_csv(UNISON_CSV),
            [Notes(67), Notes(69)],
        ),
    ]


@pytest.mark.parametrize("df, expected", test_cases())
def test_eval(df, expected):
    assert MelodyExtractor.get_melody(df) == NoteProgression(expected)
