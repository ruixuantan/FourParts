from copy import deepcopy
import json


def _shift_pitch(pitches):
    """
    Removes the last element of pitches and
    appends to the front. Mutable operation.

    Attributes
    ----------
    pitches : list of int
    """

    last_pitch = pitches.pop()
    pitches.insert(0, last_pitch)


def _zero(pitches):
    """
    Subtracts away the value of the first element from all elements.

    Attributes
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
        if pitches[i] < 0:
            pitches[i] += 12

    return pitches


def _minimise_interval(pitches):
    """
    Finds the number of pitch shifts in order to minimise
    the intervals. Assumes that pitch has been sorted.

    Attributes
    ----------
    pitches : list of int
        Should have been pre-sorted.

    Returns
    -------
    int
        The number of shifts required.
    """

    # want to minimise `greatest_interval`
    # maximum value of interval is always 12
    n = 0
    greatest_interval = 12
    size = len(pitches)

    for i in range(size):
        curr_interval = pitches[size - 1] - pitches[0]

        if curr_interval < 0:
            curr_interval += 12

        if curr_interval < greatest_interval:
            greatest_interval = curr_interval
            n = i

        _shift_pitch(pitches)

    return n


class PitchClassSet():

    def __init__(self, pitches, name):
        """
        A class that represents pitch class sets.

        Attributes
        ----------
        pitches : tuple of int
            The pitches of fragment being analysed,
            already in normal form.
        name : str
            Name of the pitch class set.
        """

        self.pitches = pitches
        self.name = name

    @staticmethod
    def normalise(input_pitches):
        """
        Removes duplicate pitches and returns
        the normalised form of the set of pitches being analysed.

        Attributes
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
        pitches.sort()

        # subtracts the smallest pitch value then apply modulo 12
        pitches = list(map(lambda p : (p - pitches[0]) % 12, pitches))
        # removes duplicate pitches
        pitches = list(set(pitches))
        pitches.sort()
        n = _minimise_interval(pitches)

        for _ in range(n):
            _shift_pitch(pitches)

        return tuple(_zero(pitches))

    @staticmethod
    def get_pitch_class_set_name(pitches):
        """
        Finds the pitch class set name in PitchClassSetNames.json.

        Attributes
        ----------
        input_pitches : list of int
            This should have been normalised already.

        Returns
        -------
        str
            The name of the pitch class set. 
            If it does not exist, returns 'Not Found'.

        Notes
        -----
        PitchClassSetName.json is structured in such a way where
        each pitch class set is grouped into its cardinality.
        To find the corresponding name, iterate through all the sub names.
        """

        with open('fourparts/music_structures/PitchClassSet/PitchClassSetNames.json') as f:
            names = json.load(f)['PitchClassSetNames']

        size = len(pitches)

        try:
            for key in names[size]:
                if names[size][key] == pitches:
                    return key
        except KeyError:
            pass

        return "Not Found"

    @staticmethod
    def create_pitch_class_set(input_pitches):
        """
        Factory method to create an instance of PitchClassSet.

        Attributes
        ----------
        input_pitches : list of int

        Returns
        -------
        PitchClassSet
        """

        pitches = PitchClassSet.normalise(input_pitches)
        name = PitchClassSet.get_pitch_class_set_name(pitches)

        return PitchClassSet(pitches, name)


