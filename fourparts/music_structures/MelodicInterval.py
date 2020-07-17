from enum import Enum


class MelodicInterval(Enum):
    """Class to define the different Melodic Intervals.
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

    @staticmethod
    def get_melodic_interval(bottom_note, top_note):
        """Gets the interval when given 2 notes.

        Parameters
        ----------
        bottom_note : int
        top_note : int
            `note_top` must be of a greater int value than `note_bottom`.

        Returns
        -------
        MelodicInterval

        Raises
        ------
        Exception
            If top_note < bottom_note.
        """

        if top_note >= bottom_note:
            interval = (top_note - bottom_note) % 12
            return MelodicInterval(interval)

        else:
            raise Exception("Top note must be greater or equal to Bottom note.")
