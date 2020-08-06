from fourparts.music_structures.Notes import Notes


class NoteFrequencies:
    """A class to count the number of notes within the
    processed csv file of the midi sample.

    Attributes
    ----------
    note_count : dict of str
        The count of each note within the csv file.
    """

    def __init__(self):
        """Initialises `note_count` given from the Notes class.

        An example:
            self.note_count = {
                'C': 0,
                'C#/Db': 0,
                'D': 0,
                ...
            }
        """

        self.note_count = {key: 0 for key in Notes.get_note_names()}

    def __str__(self):
        return str(self.note_count)

    def count(self, df):
        """Counts the number of notes based on an already processed csv_file.

        Parameters
        ----------
        df : pandas.DataFrame
            Index: RangeIndex
            Columns:
                Name: Events, dtype: str
                    Must contain values of 'Note_on_c'
                Name: Note_values, dtype: int64

        Returns
        -------
        self
        """

        count_df = df[df['Events'] == 'Note_on_c']

        for _, row in count_df.iterrows():
            curr_note = Notes.create_note(row['Note_values'])
            self.note_count[curr_note] += 1

        return self

    def to_csv(self, filename='note_frequencies.csv'):
        """Converts self.note_count to a csv file.

        Parameters
        ----------
        filename : str
            The filename where the csv file is to be saved.
            Default is given as 'note_frequencies.csv'.
        """

        if filename[-4:] != '.csv':
            filename += '.csv'

        with open(filename, 'w') as f:
            f.write("Note,Count\n")
            for key in self.note_count.keys():
                f.write("%s,%s\n" % (key, self.note_count[key]))
