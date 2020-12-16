from fourparts.exceptions.NoteOrderException import NoteOrderException
from fourparts.structures.voices.Voice import Bass, Soprano
from fourparts.structures.voices.VoicingInterval import BassSoprano


class Dyad:
    """A collection of 2 `Voice`s, sorted in ascending order.
    Uses the `Bass` and `Soprano` `Voice`s.

    Attributes
    ----------
    bass, soprano : Voice
    """

    def __init__(self, bass, soprano):
        """Constructor method.

        Parameters
        ----------
        bass, soprano : int

        Raises
        ------
        NoteOrderException
            If order if notes input is wrong.
        """

        if not bass <= soprano:
            raise NoteOrderException("Notes are out of order.")

        self.bass = Bass(bass)
        self.soprano = Soprano(soprano)

    def __str__(self):
        return "Bass:{0}, Soprano: {1}".format(self.bass, self.soprano)

    def __eq__(self, other):
        return (
            self.__class__ == other.__class__
            and self.bass == other.bass
            and self.soprano == other.soprano
        )

    def get_interval(self):
        """Gets the melodic interval between the 2 notes.

        Returns
        -------
        MelodicInterval
        """

        return BassSoprano.create_voicing_interval(
            self.bass, self.soprano
        ).melodic_interval
