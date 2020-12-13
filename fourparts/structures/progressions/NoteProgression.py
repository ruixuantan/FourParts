from fourparts.structures.MelodicInterval import MelodicInterval


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

    def __iter__(self):
        return self

    def __len__(self):
        return self.high

    def __next__(self):
        self.current += 1

        if self.current < self.high:
            return self.progression[self.current]

        raise StopIteration

    def get_intervals(self):
        """Gets the melodic intervals between Notes in the progression.

        Returns
        -------
        list of MelodicIntervals
        """

        interval_list = []
        for i in range(len(self.progression) - 1):
            melodic_interval = MelodicInterval.get_melodic_interval(self.progression[i].note_int,
                                                                    self.progression[i + 1].note_int)
            interval_list.append(melodic_interval)

        return interval_list
