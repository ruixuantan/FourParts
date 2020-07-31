from fourparts import get_note_events
from fourparts.processes.NoteEvent import NoteEvent

import pandas as pd
import pytest


def test_cases():
    test_cases = [
        (
            pd.DataFrame({'Timings': [1], 'Note_values': [4], 'Events': ['Note_on_c']}), 
            1, [NoteEvent(4, True)]
        ),
        (
            pd.DataFrame({'Timings': [1, 1], 'Note_values': [4, 6], 
                          'Events': ['Note_on_c', 'Note_off_c']}), 
            1, [NoteEvent(6, False), NoteEvent(4, True)]
        ),
        (
            pd.DataFrame({'Timings': [0, 3], 'Note_values': [4, 6],
                          'Events': ['Note_off_c', 'Note_off_c']}), 
            0, [NoteEvent(4, False)]
        ),
        (
            pd.DataFrame({'Timings': [1, 1, 3], 'Note_values': [11, 1, 11], 
                          'Events': ['Note_on_c', 'Note_off_c', 'Note_on_c']}), 
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

