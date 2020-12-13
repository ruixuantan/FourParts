TONEROW_LENGTH = 12


class ToneRow:
    """Represents a tone row.

    Attributes
    ----------
    tone_row : NoteProgression
        current : int
    current : int
        To allow ToneRow to be iterable.
    high : int
        To allow ToneRow to be iterable.
    """

    def __init__(self, tone_row):
        """Constructor method.

        Parameters
        ----------
        tone_row : NoteProgression
        """
        if not ToneRow.is_valid_tone_row(tone_row):
            raise ToneRowException

        self.tone_row = tone_row
        self.current = -1
        self.high = TONEROW_LENGTH

    def __iter__(self):
        return self

    def __len__(self):
        return self.high

    def __next__(self):
        self.current += 1

        if self.current < self.high:
            return self.progression[self.current]

        raise StopIteration

    @classmethod
    def is_valid_tone_row(cls, tone_row):
        """Checks if given tone_row is valid.

        Parameters
        ----------
        tone_row : NoteProgression

        Returns
        -------
        boolean
        """

        if len(tone_row) != TONEROW_LENGTH:
            return False

        valid_tone_row = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        pitch_list = []
        for note in tone_row:
            pitch_list.append(note.note_int % 12)

        return set(pitch_list) == set(valid_tone_row)


class ToneRowException(Exception):
    """Exception raised when ToneRow is not valid.
    """

    pass

