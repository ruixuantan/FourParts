from fourparts.music_structures.Chord import Chord
from fourparts.music_structures.MelodicInterval import MelodicInterval
from fourparts.music_structures.PitchClassSet.PitchClassSet import PitchClassSet

import pandas as pd


class ChordProgression:

    def __init__(self, progression):
        """Constructor method for ChordProgression.

        Attributes
        ----------
        progression : list of Chord
        """

        self.progression = progression

    def get_pitch_class_sets(self):
        """Gets the pitch class sets of the chords.

        Returns
        -------
        list of PitchClassSet
        """

        pitch_class_sets = []

        for chord in self.progression:
            pitch_class_set = chord.get_pitch_class_set()
            pitch_class_sets.append(pitch_class_set)

        return pitch_class_sets

    def check_parallels(self):
        """Checks the entire progression for parallel fifths and octaves.
        If 2 notes remain static, it is not considered parallel.

        Returns
        -------
        list of dict
            Each dict is obtained from the attribute in Result.
        """

        results = []

        for i in range(len(self.progression) - 1):

            curr_chord = self.progression[i]
            next_chord = self.progression[i + 1]
            sub_result = curr_chord.check_parallel_intervals(next_chord)

            results.append(sub_result)

        return results 
            