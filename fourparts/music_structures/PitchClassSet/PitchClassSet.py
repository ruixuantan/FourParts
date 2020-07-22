from copy import deepcopy

from fourparts.music_structures.PitchClassSet.PitchClassSetNames import PITCH_CLASS_SET_NAMES


def _shift_twelve(number):
    """Shifts the number by 12, if it is less than 0.

    Parameters
    ----------
    number : int

    Returns
    -------
    int
    """

    if number < 0:
        number += 12
    return number


def _shift_pitch(pitches):
    """Removes the last element of pitches and
    appends to the front. Mutable operation.

    Parameters
    ----------
    pitches : list of int
    """

    last_pitch = pitches.pop()
    pitches.insert(0, last_pitch)


def _zero(pitches):
    """Subtracts away the value of the first element from all elements.

    Parameters
    ----------
    pitches : list of int

    Returns
    -------
    list of int
        The transformed pitches.
    """

    first_pitch = pitches[0]
    for i in range(len(pitches)):
        pitches[i] -= first_pitch
        pitches[i] = _shift_twelve(pitches[i])

    return pitches


def _get_interval_distances(pitches):
    """Gets the interval (distance) between the
    first and each note.

    Parameters
    ----------
    pitches : list of int

    Returns
    -------
    list of int
    """

    distances = []
    # put the furthest interval distance in front.
    for i in range(len(pitches) - 1, 0, -1):
        distance = _shift_twelve(pitches[i] - pitches[0])
        distances.append(distance)

    return distances


def _minimise_interval(pitches):
    """Finds the number of pitch shifts in order to minimise
    the intervals. Assumes that pitch has been sorted.

    Parameters
    ----------
    pitches : list of int
        Should have been pre-sorted.

    Returns
    -------
    int
        The number of shifts required.
    """

    # want to minimise `least_distances`
    number_of_shifts = 0
    least_distances = _get_interval_distances(pitches)
    _shift_pitch(pitches)

    for i in range(1, len(pitches)):
        curr_distances = _get_interval_distances(pitches)

        for c, l in zip(curr_distances, least_distances):
            if c < l:
                least_distances = curr_distances
                number_of_shifts = i
                break
            elif c > l:
                break

        _shift_pitch(pitches)

    return number_of_shifts


class PitchClassSet():
    """A class that represents pitch class sets.

    Attributes
    ----------
    pitches : tuple of int
        The pitches of the musical fragment being analysed,
        already in normalised form.
    name : str
        Name of the pitch class set.
    """

    def __init__(self, pitches, name):
        """Consturctor method.

        Parameters
        ----------
        pitches : tuple of int
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
    def normalise(cls, input_pitches):
        """Removes duplicate pitches and returns
        the normalised form of the set of pitches being analysed.

        Parameters
        ----------
        input_pitches : list of int

        Returns
        -------
        tuple of int
            The normalised form of pitches.

        Notes
        -----
        Uses the algorithm of checking all cyclic permutations
        of pitches and determining which has the smallest interval.

        Raises
        ------
        Exception
            If the size of pitches is less than 2.
        """

        if len(input_pitches) < 2:
            raise Exception("Ensure there are more than 2 pitches.")

        pitches = deepcopy(input_pitches)

        # subtracts the smallest pitch value then apply modulo 12
        pitches = list(map(lambda p: (p - pitches[0]) % 12, pitches))
        # removes duplicate pitches
        pitches = list(set(pitches))
        pitches.sort()
        number_of_shifts = _minimise_interval(pitches)

        for _ in range(number_of_shifts):
            _shift_pitch(pitches)

        return tuple(_zero(pitches))

    @classmethod
    def hash_pitch_class_set(cls, pitches):
        """Gets the hash of the pitches.

        Parameters
        ----------
        pitches : list of int

        Returns
        -------
        str
            The string of concatenated pitches.
            This is guaranteed to be unique.
        """

        string = ''
        for pitch in pitches:
            string += str(pitch)

        return string

    @classmethod
    def get_pitch_class_set_name(cls, pitches):
        """Finds the pitch class set name in PitchClassSetNames.json.

        Parameters
        ----------
        input_pitches : list of int
            This should have been normalised already.

        Returns
        -------
        str
            The name of the pitch class set.
            If it does not exist, returns 'Not Named'.

        Notes
        -----
        PitchClassSetNames.py is structured in such a way where
        each pitch class set is grouped into its cardinality.
        Within each group is a dictionary of Pitch Class Sets.
        """

        names = PITCH_CLASS_SET_NAMES['PitchClassSetNames']
        size = len(pitches)
        key = cls.hash_pitch_class_set(pitches)

        try:
            return names[size][key]
        except KeyError:
            pass

        return "Not Named"

    @classmethod
    def create_pitch_class_set(cls, input_pitches):
        """Factory method to create an instance of PitchClassSet.

        Parameters
        ----------
        input_pitches : list of int

        Returns
        -------
        PitchClassSet
        """

        pitches = PitchClassSet.normalise(input_pitches)
        name = PitchClassSet.get_pitch_class_set_name(list(pitches))

        return cls(pitches, name)
