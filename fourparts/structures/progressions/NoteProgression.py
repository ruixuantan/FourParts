from fourparts.structures.MelodicInterval import MelodicInterval


class NoteProgression:
    """Represents a progression of notes.

    Attributes
    ----------
    progression : list of Notes
    """

    def __init__(self, progression):
        """Constructor method.

        Parameters
        ----------
        progression : list of Notes
        """

        self.progression = progression

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
