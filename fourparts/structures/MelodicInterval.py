from enum import Enum


class Interval(Enum):
    """Represents different Melodic Intervals."""

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
    def get_interval(cls, bottom_note_int, top_note_int):
        """Gets the interval when given 2 notes.

        Parameters
        ----------
        bottom_note_int : int
        top_note_int : int

        Returns
        -------
        Interval
        """

        interval = top_note_int - bottom_note_int

        if top_note_int < bottom_note_int:
            interval *= -1

        return cls(interval % 12)


class Order(Enum):
    """Represents the order of an interval.
    For example, if the interval is ascending, descending or static.
    """

    Static = 0
    Ascending = 1
    Descending = -1

    @classmethod
    def check_order(cls, bottom_note_int, top_note_int):
        """Checks if the given 2 notes form an ascending, descending or static order.

        Parameters
        ----------
        bottom_note_int : int
        top_note_int : int

        Returns
        -------
        Order
        """

        difference = top_note_int - bottom_note_int
        if difference == 0:
            return Order.Static
        elif difference > 0:
            return Order.Ascending
        elif difference < 0:
            return Order.Descending

        assert False

    def swap_order(self):
        """Swaps order.
        For example, changes Ascending to Descending and Descending to Ascending.
        Static remains Static

        Returns
        -------
        Order
        """

        return Order(self.value * -1)


class MelodicInterval:
    """Represents an actual MelodicInterval.

    Attributes
    ----------
    interval : Interval
    order : Order
    octaves : int
        Number of octaves separating the 2 notes.
    """

    def __init__(self, interval, order, octaves):
        """Constructor method.

        Parameters
        ----------
        interval : Interval
        order : Order
        octaves : int
        """

        self.interval = interval
        self.order = order
        self.octaves = octaves

    def __eq__(self, other):
        return (
            self.__class__ == other.__class__
            and self.interval == other.interval
            and self.order == other.order
            and self.octaves == other.octaves
        )

    @classmethod
    def create_melodic_interval(cls, bottom_note_int, top_note_int):
        """Constructs a MelodicInterval given 2 note integers,

        Parameters
        ----------
        bottom_note_int : int
        top_note_int : int

        Returns
        -------
        MelodicInterval
        """

        number_of_octaves = (top_note_int - bottom_note_int) // 12
        if number_of_octaves < 0:
            number_of_octaves = (number_of_octaves + 1) * -1

        return cls(
            Interval.get_interval(bottom_note_int, top_note_int),
            Order.check_order(bottom_note_int, top_note_int),
            number_of_octaves,
        )

    def swap_order(self):
        """Changes a MelodicInterval with Ascending Order to Descending Order and
        vice versa.

        Returns
        -------
        MelodicInterval
        """

        new_order = self.order.swap_order()
        return MelodicInterval(self.interval, new_order, self.octaves)

    def create_note_int(self, note_int):
        """Generates a note_int based on MelodicInterval.

        Parameters
        ----------
        note_int : int

        Returns
        -------
        int
        """

        if self.order == Order.Static:
            return note_int

        octave_intervals = self.octaves * 12

        if self.order == Order.Ascending:
            new_note_int = note_int + self.interval.value + octave_intervals
        elif self.order == Order.Descending:
            new_note_int = note_int - self.interval.value - octave_intervals

        # TODO: Find more elegant way of avoiding negative Note values.
        while new_note_int < 0:
            new_note_int += 12

        return new_note_int
