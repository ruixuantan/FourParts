from enum import Enum


class MelodicInterval(Enum):
    """Represents different Melodic Intervals.
    """

    # TODO: to include augmented and diminished intervals
    Octave = 0
    Semitone = 1
    Tone = 2
    MinorThird = 3
    MajorThird = 4
    PerfectFourth = 5
    Tritone = 6
    PerfectFifth = 7
    MinorSixth = 8
    MajorSixth = 9
    MinorSeventh = 10
    MajorSeventh = 11

    @classmethod
    def get_melodic_interval(cls, bottom_note, top_note):
        """Gets the interval when given 2 notes.

        Parameters
        ----------
        bottom_note : int
        top_note : int

        Returns
        -------
        MelodicInterval
        """

        interval = top_note - bottom_note

        if top_note < bottom_note:
            interval *= -1

        return cls(interval % 12)
