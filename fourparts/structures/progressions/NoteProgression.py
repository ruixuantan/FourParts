from fourparts.structures.notes.Notes import Notes
from fourparts.structures.MelodicInterval import Interval


class NoteProgression:
    """Represents a progression of notes.

    Attributes
    ----------
    progression : list of Notes
    current : int
        To allow NoteProgression to be iterable.
    high : int
        To allow NoteProgression to be iterable.
    """

    def __init__(self, progression):
        """Constructor method.

        Parameters
        ----------
        progression : list of Notes
        """

        self.progression = progression
        self.current = -1
        self.high = len(progression)

    def __eq__(self, other):
        return self.progression == other.progression

    def __iter__(self):
        return self

    def __len__(self):
        return self.high

    def __next__(self):
        self.current += 1

        if self.current < self.high:
            return self.progression[self.current]

        raise StopIteration

    def __getitem__(self, index):
        return self.progression[index]

    def __repr__(self):
        return str(self.progression)

    @classmethod
    def create_note_progression(cls, note_ints):
        """Creates a NoteProgression based on a list of integers.

        Parameters
        ----------
        note_ints : list of int

        Returns
        -------
        NoteProgression
        """

        notes = [Notes(note_int) for note_int in note_ints]
        return cls(notes)

    def get_intervals(self):
        """Gets the melodic intervals between Notes in the progression.

        Returns
        -------
        list of MelodicIntervals
        """

        interval_list = []
        for i in range(len(self.progression) - 1):
            melodic_interval = Interval.get_interval(
                self.progression[i].note_int, self.progression[i + 1].note_int
            )
            interval_list.append(melodic_interval)

        return interval_list

    def reverse(self):
        """Reverses the NoteProgression.

        Returns
        -------
        NoteProgression
        """

        return NoteProgression(self.progression[::-1])
