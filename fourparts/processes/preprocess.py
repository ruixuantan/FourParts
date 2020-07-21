"""
Extracts the chords from the provided midi file.
A chord change is defined to be a change in any of the 4 notes.
For example, a chord progression of Csus4 to C is considered 2 chords.
"""

from fourparts import Chord
from fourparts.utils.NoteContainer import NoteContainer
from fourparts.utils.NoteEvent import NoteEvent

import pandas as pd
import py_midicsv


def midi_to_df(midi_file, save=False):
    """Converts a midi file to a list of csv then to a pandas df.

    Parameters
    ----------
    midi_file : str
        The directory pointing towards the midi file to be converted.
    save : bool, optional
        If specified, saves `midi_file` as a csv in the same directory
        and as the same name.

    Returns
    -------
    pandas.DataFrame
        A DataFrame that contains the timing of note events and note values,
        amongst other (irrelevant) information.

    Raises
    ------
    Exception
        If `midi_file` is not pointing towards a .mid file.
    """

    if midi_file[-4:] != '.mid':
        raise Exception("Pass in a .mid file!")

    csv_string = py_midicsv.midi_to_csv(midi_file)
    df = pd.DataFrame([ls.strip().split(',') for ls in csv_string])

    # convert values to int
    df[0] = df[0].fillna(0).astype(int)
    df[1] = df[1].fillna(0).astype(int)
    df[2] = df[2].str.strip()
    df[4] = df[4].str.strip().fillna(0).replace('"major"', 0).astype(int)
    df[5] = df[5].fillna(0).astype(int)

    # rename df columns
    df = df.rename(columns={0: 'Track_id',
                            1: 'Timings',
                            2: 'Events',
                            3: 'Time_signatures',
                            4: 'Note_values',
                            5: 'Velocity'})

    if save:
        df.to_csv(midi_file[:-4] + '.csv')

    return df


def get_note_events(df, time):
    """Gets a list of note events, sorted in ascending order,
    based on the given time.

    Parameters
    ----------
    df : pandas.DataFrame
        Index: RangeIndex
        Columns:
            Name: Timings, dtype: int64
            Name: Note_values, dtype: int64
            NameL Velocity, dtype: int64
    time : int
        The timing selected.

    Returns
    -------
    list of NoteEvent

    Notes
    -----
    Key assumption that velocity associated with a note-on event is > 0
    and velocity of note-off event = 0.
    """
    df_chord_notes = df[df['Timings'] == time]
    chord_notes = df_chord_notes['Note_values'].to_list()
    chord_notes.sort()
    
    events = []

    for note in chord_notes:
        on = df_chord_notes[df_chord_notes['Note_values'] == note]['Velocity'].iloc[0] > 0
        events.append(NoteEvent(note, on))

    return events


def get_chord_progression(df):
    """Creates a list of chord progression based on the input notes.

    Parameters
    ----------
    df : pandas.DataFrame
        Index: RangeIndex
        Columns:
            Name: Track_id, dtype: int64 
            Name: Timings, dtype: int64
            Name: Events, dtype: str
            Name: Time_signatures, dtype: int64
            Name: Note_values, dtype: int64 
            Name: Velocity, dtype: int64
            Name: 6, dtype: int64 (?)

    Returns
    -------
    list of Chord
        A list of the chords.
    """

    df_all_notes = df[df['Events'] == 'Note_on_c']
    timings = df_all_notes['Timings'].unique()
    timings.sort()
    # remove timing = 0
    if timings[0] == 0:
        timings = timings[1:]

    first_chord_note_events = get_note_events(df_all_notes, 0)
    first_chord_notes = [event.note for event in first_chord_note_events]

    container = NoteContainer.create_container(first_chord_notes)
    first_chord = container.create_chord()

    progression = [first_chord]

    for time in timings:
        note_events = get_note_events(df_all_notes, time)

        for event in note_events:
            if event.on:
                chord = container.update_note_on(event.note)
                if isinstance(chord, Chord):
                    progression.append(chord)
            else:
                container.update_note_off(event.note)

    return progression
