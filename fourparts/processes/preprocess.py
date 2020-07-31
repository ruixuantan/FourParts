"""
Extracts the chords from the provided midi file.
A chord change is defined to be a change in any of the 4 notes.
For example, a chord progression of Csus4 to C is considered 2 chords.
"""
from fourparts.processes.DyadContainer import DyadContainer
from fourparts.processes.ChordContainer import ChordContainer
from fourparts.processes.NoteEvent import NoteEvent

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
    ValueError
        If `midi_file` is not pointing towards a .mid file.
    """

    if midi_file[-4:] != '.mid':
        raise ValueError("Pass in a .mid file!")

    csv_string = py_midicsv.midi_to_csv(midi_file)
    df = pd.DataFrame([ls.strip().split(',') for ls in csv_string])

    # convert values to int
    df[0] = df[0].fillna(0).astype(int)
    df[1] = df[1].fillna(0).astype(int)
    df[2] = df[2].str.strip()
    df[4] = df[4].str.strip().fillna(0).replace('"major"', 0).astype(int)
    df[5] = df[5].fillna(0).astype(int)

    # convert note velocity of 0 to 'Note_off_c' events
    # Key assumption that note velocity of 0 equals to a note off event
    df[2].loc[(df[5] == 0) & (df[2] == 'Note_on_c')] = 'Note_off_c'
    
    # rename df columns
    df = df.rename(columns={0: 'Track_id',
                            1: 'Timings',
                            2: 'Events',
                            3: 'Time_signatures',
                            4: 'Note_values',
                            5: 'Velocity'})

    df.to_csv(midi_file[:-4] + '.csv') if save else None
    return df


def get_note_events(df, time):
    """Gets a list of note events, sorted in ascending order,
    based on the given time. Note events of 'off' are placed in front.

    Parameters
    ----------
    df : pandas.DataFrame
        Index: RangeIndex
        Columns:
            Name: Timings, dtype: int64
            Name: Note_values, dtype: int64
            Name: Events, dtype: str
    time : int
        The timing selected.

    Returns
    -------
    list of NoteEvent
    """

    df_chord_notes = df[df['Timings'] == time]
    chord_notes = df_chord_notes['Note_values'].to_list()
    chord_notes.sort()

    on_events = []
    off_events = []

    for note in chord_notes:
        idx = df_chord_notes[df_chord_notes['Note_values'] == note]['Events'].index[0]
        on = df_chord_notes['Events'].loc[idx] == 'Note_on_c'
        df_chord_notes = df_chord_notes.drop(idx)

        if on:
            on_events.append(NoteEvent(note, True))
        else:
            off_events.append(NoteEvent(note, False))

    return off_events + on_events


class PreProcessor:
    """A class that converts a midi converted DataFrame
    to a list of music structures: either Chord or VoicingInterval.

    Attributes
    ----------
    container : Dyad or Chord Container
        """

    def __init__(self, n):
        """Constructor method for PreProcessor.
        
        Parameters
        ----------
        n : int
            2 for DyadContainer
            4 for ChordContainer

        Raises
        ------
        ValueError
            When n passed in has not been implemented.
        """
        if n == 2:
            self.container = DyadContainer
        elif n == 4:
            self.container = ChordContainer
        else:
            raise ValueError("Only Dyads and Chords are implemented.")

    def get_progression(self, df):
        """Creates a progression based on the input notes.

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
        list of music structure
            Currently, either list of Chords or VoicingIntervals.
        """

        df_all_notes = df[(df['Events'] == 'Note_off_c') | (df['Events'] == 'Note_on_c')]
        timings = df_all_notes['Timings'].unique()
        timings.sort()
        first_timing = timings[0]
        timings = timings[1:]

        first_note_events = get_note_events(df_all_notes, first_timing)
        first_container_notes = [event.note for event in first_note_events]

        container = self.container.create_container(first_container_notes)
        first_filled_container = container.create_music_structure()

        progression = [first_filled_container]

        for time in timings:
            note_events = get_note_events(df_all_notes, time)

            for event in note_events:
                if event.on:
                    filled_container = container.update_note_on(event.note)
                    if filled_container is not None:
                        progression.append(filled_container)
                else:
                    container.update_note_off(event.note)

        return progression
