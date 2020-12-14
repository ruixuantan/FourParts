from fourparts.structures.MelodicInterval import MelodicInterval


NOTE_VALUE_EXCEPTION_MESSAGE = "Ensure note value is greater than 0."


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
            raise ValueError(NOTE_VALUE_EXCEPTION_MESSAGE)

        self.note_int = note_int

    def __eq__(self, other):
        return self.note_int == other.note_int

    def __repr__(self):
        return str(self.note_int)

    @classmethod
    def create_base_note(cls, note_int):
        """Creates a base note.
        A base note has a value from 0 to 11.

        Parameter
        ---------
        note_int : int

        Returns
        -------
        Notes

        Raises
        ------
        ValueException
            If the value of note_int is negative
        """

        if note_int < 0:
            raise ValueError(NOTE_VALUE_EXCEPTION_MESSAGE)

        return Notes(note_int % 12)

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

    def create_note_with_melodic_interval(self, melodic_interval):
        """Creates note based on the MelodicInterval.

        Parameters
        ----------
        melodic_interval : MelodicInterval

        Returns
        -------
        Notes
        """

        new_note_int = melodic_interval.create_note_int(self.note_int)
        assert new_note_int >= 0
        return Notes(new_note_int)
