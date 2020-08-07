from fourparts import NoteFrequencies
import pandas as pd 
import pytest


def test_cases():
    test_cases = [
        (
            pd.DataFrame({'Events': ['Note_on_c', 'Note_on_c', 'Note_on_c'], 
                          'Note_values': [60, 61, 62]}),
            {'C':1, 'C#/Db':1, 'D':1, 'D#/Eb':0, 'E':0, 'F':0, 'F#/Gb':0, 'G':0, 'G#/Ab':0, 'A':0, 'A#/Bb':0, 'B': 0}
        ),
        (
            pd.DataFrame({'Events': ['Note_on_c', 'Note_on_c'], 
                          'Note_values': [60, 65]}),
            {'C':1, 'C#/Db':0, 'D':0, 'D#/Eb':0, 'E':0, 'F':1, 'F#/Gb':0, 'G':0, 'G#/Ab':0, 'A':0, 'A#/Bb':0, 'B': 0}
        )
    ]

    return test_cases


@pytest.mark.parametrize("df, expected", test_cases())
def test_eval(df, expected):
    assert NoteFrequencies().count(df).note_count == expected
