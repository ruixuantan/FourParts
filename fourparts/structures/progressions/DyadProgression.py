class DyadProgression:
    """Represents 2 part writing.

    Attributes
    ----------
    progression : list of Dyads
    """

    def __init__(self, progression):
        """Constructor method.

        Parameters
        ----------
        progression : list of Dyads
        """

        self.progression = progression

    def get_harmonic_intervals(self):
        """Gets the melodic intervals of the `Dyads`.

        Returns
        -------
        list of MelodicInterval
        """

        return [dyad.get_interval() for dyad in self.progression]
