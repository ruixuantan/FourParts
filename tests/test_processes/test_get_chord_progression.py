from fourparts import Chord, PreProcessor
import pandas as pd
import pytest


def test_cases():
    test_cases = [
        (
            pd.read_csv('samples/perfect_cadence.csv'),
            [Chord(50, 57, 60, 65),
             Chord(43, 59, 62, 65),
             Chord(48, 55, 60, 64)]
        ),
        (
            pd.read_csv('samples/typeA_perfect_cadence.csv'),
            [Chord(53, 57, 60, 64),
             Chord(53, 57, 59, 64),
             Chord(52, 55, 57, 62)]
        ),
        (
            pd.read_csv('samples/chorale_F.csv'),
            [Chord(41, 57, 60, 65),
             Chord(46, 58, 62, 65),
             Chord(46, 58, 64, 67),
             Chord(41, 60, 65, 69),
             Chord(43, 58, 62, 67),
             Chord(45, 57, 62, 65),
             Chord(45, 57, 62, 64),
             Chord(45, 55, 61, 64),
             Chord(38, 53, 57, 62)]
        )
    ]

    return test_cases


@pytest.mark.parametrize("df, expected", test_cases())
def test_eval(df, expected):
    assert PreProcessor(4).get_progression(df) == expected


def exception_cases():
    exception_cases = [
        (
            pd.DataFrame({'events': ['Note_on_c', 'Note_on_c', 'Note_on_c', 'Note_on_c'], 
                          'Timings': [0, 0, 0, 0],
                          'Note_values': [3, 4, 5, 6],
                          'Velocity': [80, 80, 80, 80]}), 
            pytest.raises(KeyError)
        ),
        (
            pd.DataFrame({'events': ['Note_on_c', 'Note_on_c', 'Note_on_c', 'Note_on_c'], 
                          'Timings': [0, 0, 0, 0]}), 
            pytest.raises(KeyError)
        ),
        (
            pd.DataFrame({'Events': ['Note_on_c', 'Note_on_c', 'Note_on_c'], 
                          'Timings': [0, 0, 0],
                          'Note_values': [3, 4, 5],
                          'Velocity': [80, 80, 80]}), 
            pytest.raises(Exception)
        ),
    ]

    return exception_cases


@pytest.mark.parametrize("df, exception", exception_cases())
def test_eval(df, exception):
    with exception:
        assert PreProcessor(4).get_progression(df) is not None
