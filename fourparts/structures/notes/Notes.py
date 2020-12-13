class Notes:
    """A class to define notes, based on the midi input.
    """

    NOTES = (
        'C',  # 0
        'C#/Db',  # 1
        'D',  # 2
        'D#/Eb',  # 3
        'E',  # 4
        'F',  # 5
        'F#/Gb',  # 6
        'G',  # 7
        'G#/Ab',  # 8
        'A',  # 9
        'A#/Bb',  # 10
        'B'  # 11
    )

    def __init__(self, note_int):
        """Constructor method.

        Parameters
        ----------
        note_int : int
            Expected to be less than 12.

        Raises
        ------
        ValueError
            If note_int is lesser than 0.
        """

        if note_int < 0:
            raise ValueError('Ensure note value is greater than 0.')

        self.note_int = note_int

    def __eq__(self, other):
        return self.note_int == other.note_int

    def get_note_name(self):
        """Gets the name of the note.

        Parameters
        ----------
        str
            Name of the note.
        """

        return Notes.NOTES[self.note_int]

    @classmethod
    def get_note_names(cls):
        """Gets the notes defined in this class.

        Returns
        -------
        tuple of str
            NOTES
        """

        return Notes.NOTES

    @classmethod
    def get_note_index(cls, note):
        """Gets the index of the note in NOTES.

        Parameters
        ----------
        note : str

        Returns
        -------
        int
            Ranges from 0 to 11.

        Raises
        ------
        KeyError
            If `note` does not exist in NOTES.
        """

        if note in Notes.NOTES:
            return Notes.NOTES.index(note)
        else:
            raise KeyError("Given note does not exist.")

    def create_note_with_melodic_interval(self, melodic_interval, is_ascending):
        """Creates note based on the MelodicInterval and if it is ascending or descending.

        Parameters
        ----------
        melodic_interval : MelodicInterval
        is_ascending : boolean

        Returns
        -------
        Notes
        """

        if is_ascending:
            new_note_int = self.note_int + melodic_interval.value
        else:
            new_note_int = self.note_int - melodic_interval.value

        return Notes(new_note_int)
