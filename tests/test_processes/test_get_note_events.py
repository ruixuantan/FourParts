from fourparts import get_note_events
from fourparts.utils.NoteEvent import NoteEvent

import pandas as pd
import pytest


def test_cases():
    test_cases = [
        (
            pd.DataFrame({'Timings': [1], 'Note_values': [4], 'Velocity': [2]}), 
            1, [NoteEvent(4, True)]
        ),
        (
            pd.DataFrame({'Timings': [1, 1], 'Note_values': [4, 6], 'Velocity': [20, 0]}), 
            1, [NoteEvent(4, True), NoteEvent(6, False)]
        ),
        (
            pd.DataFrame({'Timings': [0, 3], 'Note_values': [4, 6], 'Velocity': [0, 0]}), 
            0, [NoteEvent(4, False)]
        ),
        (
            pd.DataFrame({'Timings': [1, 1, 3], 'Note_values': [11, 1, 11], 'Velocity': [2, 0, 912]}), 
            1, [NoteEvent(1, True), NoteEvent(11, False)]
        )
    ]

    return test_cases


@pytest.mark.parametrize("df, time, expected", test_cases())
def test_eval(df, time, expected):
    
    note_events = get_note_events(df, time)

    for event, ex in zip(note_events, expected):
        if event.note != ex.note and event.on != ex.on:
            assert False

    assert True

