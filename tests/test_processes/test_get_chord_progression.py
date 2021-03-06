from fourparts import Chord, PreProcessor
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
            [Chord(50, 57, 60, 65), Chord(43, 59, 62, 65), Chord(48, 55, 60, 64)],
        ),
        (
            pd.read_csv(TYPEA_PERFECT_CADENCE_CSV),
            [Chord(53, 57, 60, 64), Chord(53, 57, 59, 64), Chord(52, 55, 57, 62)],
        ),
        (
            pd.read_csv(CHORALE_F_CSV),
            [
                Chord(41, 57, 60, 65),
                Chord(46, 58, 62, 65),
                Chord(46, 58, 64, 67),
                Chord(41, 60, 65, 69),
                Chord(43, 58, 62, 67),
                Chord(45, 57, 62, 65),
                Chord(45, 57, 62, 64),
                Chord(45, 55, 61, 64),
                Chord(38, 53, 57, 62),
            ],
        ),
        (
            pd.read_csv(UNISON_CSV),
            [Chord(47, 62, 67, 67), Chord(45, 60, 67, 69)],
        ),
    ]


@pytest.mark.parametrize("df, expected", test_cases())
def test_eval(df, expected):
    assert PreProcessor(4).get_progression(df) == expected


def exception_cases():
    return [
        (
            pd.DataFrame(
                {
                    "events": ["Note_on_c", "Note_on_c", "Note_on_c", "Note_on_c"],
                    "Timings": [0, 0, 0, 0],
                    "Note_values": [3, 4, 5, 6],
                    "Velocity": [80, 80, 80, 80],
                }
            ),
            pytest.raises(KeyError),
        ),
        (
            pd.DataFrame(
                {
                    "events": ["Note_on_c", "Note_on_c", "Note_on_c", "Note_on_c"],
                    "Timings": [0, 0, 0, 0],
                }
            ),
            pytest.raises(KeyError),
        ),
        (
            pd.DataFrame(
                {
                    "Events": ["Note_on_c", "Note_on_c", "Note_on_c"],
                    "Timings": [0, 0, 0],
                    "Note_values": [3, 4, 5],
                    "Velocity": [80, 80, 80],
                }
            ),
            pytest.raises(Exception),
        ),
    ]


@pytest.mark.parametrize("df, exception", exception_cases())
def test_exception(df, exception):
    with exception:
        assert PreProcessor(4).get_progression(df) is not None
