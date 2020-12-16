from fourparts import MelodyExtractor, Notes, NoteProgression
import pandas as pd
import pytest


def test_cases():
    return [
        (
            pd.read_csv("samples/perfect_cadence.csv"),
            [Notes(65), Notes(65), Notes(64)],
        ),
        (
            pd.read_csv("samples/typeA_perfect_cadence.csv"),
            [Notes(64), Notes(64), Notes(62)],
        ),
        (
            pd.read_csv("samples/chorale_F.csv"),
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
            pd.read_csv("samples/unison.csv"),
            [Notes(67), Notes(69)],
        ),
    ]


@pytest.mark.parametrize("df, expected", test_cases())
def test_eval(df, expected):
    assert MelodyExtractor.get_melody(df) == NoteProgression(expected)
