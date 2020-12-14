from fourparts import NoteFrequencies
import pandas as pd
import pytest


def test_cases():
    return [
        (
            pd.DataFrame(
                {
                    "Events": ["Note_on_c", "Note_on_c", "Note_on_c"],
                    "Note_values": [60, 61, 62],
                }
            ),
            {
                "C": 1,
                "C#/Db": 1,
                "D": 1,
                "D#/Eb": 0,
                "E": 0,
                "F": 0,
                "F#/Gb": 0,
                "G": 0,
                "G#/Ab": 0,
                "A": 0,
                "A#/Bb": 0,
                "B": 0,
            },
        ),
        (
            pd.DataFrame(
                {"Events": ["Note_on_c", "Note_on_c"], "Note_values": [60, 65]}
            ),
            {
                "C": 1,
                "C#/Db": 0,
                "D": 0,
                "D#/Eb": 0,
                "E": 0,
                "F": 1,
                "F#/Gb": 0,
                "G": 0,
                "G#/Ab": 0,
                "A": 0,
                "A#/Bb": 0,
                "B": 0,
            },
        ),
    ]


@pytest.mark.parametrize("df, expected", test_cases())
def test_eval(df, expected):
    assert NoteFrequencies.create_note_frequencies().count(df) == expected
