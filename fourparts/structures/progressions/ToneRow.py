from fourparts.structures.notes.Notes import Notes
from fourparts.structures.MelodicInterval import MelodicInterval
from fourparts.structures.progressions.NoteProgression import NoteProgression


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
            NoteProgression must contain notes with `note_int` of 0 to 11 inclusive.
        """

        if not ToneRow.is_valid_tone_row(tone_row):
            raise InvalidToneRowException

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

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.tone_row == other.tone_row

    def __repr__(self):
        return str(self.tone_row)

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
            pitch_list.append(note.note_int)

        return set(pitch_list) == set(valid_tone_row)

    @classmethod
    def create_tone_row(cls, progression):
        """Converts `progression` into a tone row.
        `progression` need not be contained within an octave.

        Parameters
        ----------
        progression : NoteProgression

        Returns
        -------
        ToneRow
        """

        new_progression = [
            Notes.create_base_note(note.note_int) for note in progression
        ]
        note_progression = NoteProgression(new_progression)
        return cls(note_progression)

    def get_retrograde(self):
        """Gets the retrograde of the tone row.

        Returns
        -------
        ToneRow
        """

        retrograde_note_progression = self.tone_row.reverse()
        return ToneRow(retrograde_note_progression)

    def get_inverse(self):
        """Gets the inverse of the tone row.

        Returns
        -------
        ToneRow
        """

        inverse_note_progression = [self.tone_row[0]]
        curr_inverse_note = inverse_note_progression[0]

        for i in range(TONEROW_LENGTH - 1):
            curr_note = self.tone_row[i]
            next_note = self.tone_row[i + 1]

            melodic_interval = MelodicInterval.create_melodic_interval(
                curr_note.note_int, next_note.note_int
            )
            melodic_interval = melodic_interval.swap_order()

            new_note = curr_inverse_note.create_note_with_melodic_interval(
                melodic_interval
            )
            new_base_note = Notes.create_base_note(new_note.note_int)

            inverse_note_progression.append(new_base_note)
            curr_inverse_note = new_base_note

        return ToneRow(NoteProgression(inverse_note_progression))

    def get_retrograde_inverse(self):
        """Gets the retrograde inverse of the tone row.

        Returns
        -------
        ToneRow
        """

        return self.get_inverse().get_retrograde()


class InvalidToneRowException(Exception):
    """Exception raised when ToneRow is not valid."""

    pass
