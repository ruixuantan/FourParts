from fourparts.structures.notes.Notes import Notes


class NoteFrequencies:
    """A class to count the number of notes within the
    processed csv file of the midi sample.

    Attributes
    ----------
    note_count : dict of int
        The count of each note within the csv file.
    """

    def __init__(self, note_count):
        """Initialises `note_count` given from the Notes class.

        Parameters
        ----------
        note_count : dict of int
        """

        self.note_count = note_count

    @classmethod
    def create_note_frequencies(cls):
        """Factory method to create a NoteFrequency object.

        Returns
        -------
        NoteFrequency
            All values are initialised to 0.

        An example:
            self.note_count = {
                'C': 0,
                'C#/Db': 0,
                'D': 0,
                ...
            }
        """

        return cls({key: 0 for key in Notes.get_note_names()})

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
        dict of int
        """

        count_df = df[df['Events'] == 'Note_on_c']

        for _, row in count_df.iterrows():
            curr_note = Notes.create_note(row['Note_values'])
            self.note_count[curr_note] += 1

        return self.note_count

    def convert_to_percentage(self, dp=2):
        """Converts the note counts to a percentage.

        Parameter
        ---------
        dp : int
            Number of decimal places to round off percentage to.
            Default is 2.

        Returns
        -------
        dict of float
        """

        if dp < 0:
            raise ValueError("Ensure decimal place entered is a positive integer.")

        total_notes = sum(self.note_count.values())

        if total_notes == 0:
            return self.note_count

        for key in self.note_count.keys():
            percentage = self.note_count[key] / total_notes * 100
            self.note_count[key] = round(percentage, dp)

        return self.note_count

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
