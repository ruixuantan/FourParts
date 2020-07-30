from fourparts.music_structures.MelodicInterval import MelodicInterval


class DyadProgression:
    """A class to analyse 2 part writing.

    Attributes
    ----------
    progression : list of VoicingInterval
        Use the BassSoprano Voicing Interval.
    """

    def __init__(self, progression):
        """Constructor method for VoicingProgression.

        Parameters
        ----------
        progression : list of VoicingInterval (BassSoprano)
        """

        self.progression = progression

    def get_melodic_intervals(self):
        """Gets the melodic intervals of the dyads.

        Returns
        -------
        list of MelodicInterval
        """

        return [dyad.melodic_interval for dyad in self.progression]
