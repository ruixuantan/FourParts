from fourparts.structures.pitchclass.PitchClassSetMap import PITCH_CLASS_SET_MAP, NOT_NAMED
from fourparts.commons.Orbit import Orbit


def _shift_twelve(number):
    """Shifts the number by 12, if it is less than 0.

    Parameters
    ----------
    number : int

    Returns
    -------
    int
    """

    return number + 12 if number < 0 else number


def _zero(pitch_orbit):
    """Subtracts away the value of the first element from all elements in the orbit.

    Parameters
    ----------
    pitch_orbit : Orbit of int

    Returns
    -------
    Orbit
        The transformed pitches.
    """

    first_pitch = pitch_orbit.curr_elem()
    pitch_orbit.map(lambda p: _shift_twelve(p - first_pitch))
    return pitch_orbit


def get_interval_distances(pitch_orbit):
    """Gets the interval (distance) between the first and each note.
    Place the distance of the note with the largest index in front.
    For example, pitches of [0, 4, 7] will yield [7, 4].

    Parameters
    ----------
    pitch_orbit : Orbit of int

    Returns
    -------
    list of int
    """

    distances = []
    first_elem = pitch_orbit.curr_elem()
    for i in range(pitch_orbit.length() - 1, 0, -1):
        distance = _shift_twelve(pitch_orbit.get_index(i) - first_elem)
        distances.append(distance)

    return distances


def _minimise_interval(pitch_orbit):
    """Finds the number of pitch shifts in order to minimise the intervals.
    Assumes that pitches has been sorted.

    Parameters
    ----------
    pitch_orbit : Orbit of int
        Should have been pre-sorted.

    Returns
    -------
    int
        The number of shifts required.
    """

    number_of_shifts = 0

    # want to minimise `least_distances`
    least_distances = get_interval_distances(pitch_orbit)
    pitch_orbit.shift(-1)

    for i in range(1, pitch_orbit.length()):
        curr_distances = get_interval_distances(pitch_orbit)

        for c, l in zip(curr_distances, least_distances):
            if c < l:
                least_distances = curr_distances
                number_of_shifts = i
                break
            elif c > l:
                break

        pitch_orbit.shift(-1)

    return number_of_shifts


class PitchClassSet:
    """Represents pitch class sets.

    Attributes
    ----------
    pitches : list of int
        The pitches of the musical fragment being analysed, already in normalised form.
    name : str
        Name of the pitch class set.
    """

    def __init__(self, pitches, name):
        """Constructor method.

        Parameters
        ----------
        pitches : list of int
        name : str
        """

        self.pitches = pitches
        self.name = name

    def __eq__(self, other):
        return self.pitches == other.pitches and \
               self.name == other.name

    def __str__(self):
        return "Pitches: {0}, Name: {1}".format(self.pitches,
                                                self.name)

    @classmethod
    def normalise(cls, *input_pitches):
        """Removes duplicate pitches and returns
        the normalised form of the set of pitches being analysed.

        Parameters
        ----------
        input_pitches : tuple of int

        Returns
        -------
        list of int
            The normalised form of pitches.

        Notes
        -----
        Uses the algorithm of checking all cyclic permutations
        of pitches and determining which has the smallest interval.
        """

        if not input_pitches:
            return []

        pitches = list(input_pitches)

        # subtracts the smallest pitch value then apply modulo 12
        pitches = list(map(lambda p: (p - pitches[0]) % 12, pitches))
        # removes duplicate pitches
        pitches = list(set(pitches))
        pitches.sort()

        pitch_orbit = Orbit(pitches)
        number_of_shifts = _minimise_interval(pitch_orbit)

        pitch_orbit.shift(-1 * number_of_shifts)

        _zero(pitch_orbit)

        return pitch_orbit.get_curr_orbit()
        
    @classmethod
    def get_pitch_class_set_name(cls, *pitches):
        """Finds the pitch class set name in PitchClassSetNames.py.

        Parameters
        ----------
        pitches : tuple of int
            This should have been normalised already.

        Returns
        -------
        str
            The name of the pitch class set.
            If it does not exist, returns `NOT_NAMED`.

        Notes
        -----
        PitchClassSetMap.py is structured in such a way where
        each pitch class set is grouped into its cardinality.
        Within each group is a dictionary of pitch class sets.
        """

        size = len(pitches)

        try:
            return PITCH_CLASS_SET_MAP[size][pitches]
        except KeyError:
            return NOT_NAMED

    @classmethod
    def create_pitch_class_set(cls, *input_pitches):
        """Creates an instance of `PitchClassSet`.

        Parameters
        ----------
        input_pitches : tuple of int

        Returns
        -------
        PitchClassSet
        """

        pitches = PitchClassSet.normalise(*input_pitches)
        name = PitchClassSet.get_pitch_class_set_name(tuple(pitches))

        return cls(pitches, name)
