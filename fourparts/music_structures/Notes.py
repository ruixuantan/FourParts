class Notes:
    """A class to defined notes, based on the midi input.

    Attributes
    ----------
    note : str
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

    def __init__(self, note):
        """Constructor method for Note.

        Parameters
        ----------
        note : str
            A string as specified in NOTES.
        """

        self.note = note

    @classmethod
    def create_note(cls, note_int):
        """Factory method to construct a note.
        
        Parameters
        ----------
        note_int : int
            The input integer to be converted into a Note.

        Returns
        -------
        Note
        
        Raises
        ------
        ValueError
            If `note_int` is less than 0.
        """

        if note_int < 0:
            raise ValueError('Ensure note value is greater than 0.')

        actual_note_int = note_int % 12
        return cls(Notes.NOTES[actual_note_int])

    def __str__(self):
        return self.note

    def __eq__(self, other):
        return self.note == other.note
