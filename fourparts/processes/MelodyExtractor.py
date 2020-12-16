from fourparts.structures.notes.Notes import Notes
from fourparts.structures.progressions.NoteProgression import NoteProgression


class MelodyExtractor:
    """Represents class that extracts out melody given any midi file.
    Assumes that melody are notes of the highest frequency.
    """

    @classmethod
    def get_event_timings(cls, df):
        """Gets the timings of the note events in `df`.

        Parameters
        ----------
        df : pandas.DataFrame
            Index: RangeIndex
            Columns:
                Name: Timings, dtype: int64

        Returns
        -------
        list of int
            The list of timings, in ascending order.
        """

        timings = list(df["Timings"].unique())
        timings.sort()

        return timings

    @classmethod
    def get_melody(cls, df):
        """Extracts the melody of a dataframe.

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
        NoteProgression
        """

        df_all_notes = df[
            (df["Events"] == "Note_on_c")
        ]
        timings = MelodyExtractor.get_event_timings(df_all_notes)

        notes_list = []
        for time in timings:
            df_curr_notes = df_all_notes[df_all_notes["Timings"] == time]
            curr_notes = df_curr_notes["Note_values"].to_list()
            curr_notes.sort()
            greatest_note_int = curr_notes[-1]
            melody_note = Notes(greatest_note_int)
            notes_list.append(melody_note)

        return NoteProgression(notes_list)


if __name__ == "__main__":
    from fourparts.processes.PreProcessor import midi_to_df
    print(MelodyExtractor.get_melody(midi_to_df("samples/chorale_F.mid")))