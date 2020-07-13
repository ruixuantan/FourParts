from fourparts.music_structures.Chord import Chord
from fourparts.music_structures.MelodicInterval import MelodicInterval
from fourparts.utils.Result import Result

import pandas as pd


class ChordProgression:

    def __init__(self, progression):
        """Constructor method for ChordProgression.

        Attributes
        ----------
        progression : list of Chord
        """

        self.progression = progression

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

            curr_intervals = curr_chord.get_intervals()
            next_intervals = next_chord.get_intervals()

            sub_result = Result()
            # iterate through all 6 possible voicing_intervals
            for voicing_interval in curr_intervals.keys():

                curr_voicing_interval = curr_intervals[voicing_interval]
                next_voicing_interval = next_intervals[voicing_interval]

                # get the melodic interval between the voicing interval
                # etc. the perfect 4th between the C Bass note and F Alto note
                curr_melodic_interval = curr_voicing_interval.melodic_interval
                next_melodic_interval = next_voicing_interval.melodic_interval

                if curr_melodic_interval == MelodicInterval.Octave:
                    if curr_melodic_interval == next_melodic_interval:
                        if curr_voicing_interval.top_voice != next_voicing_interval.top_voice:
                            sub_result.update(voicing_interval, 'Parallel Octave')

                if curr_melodic_interval == MelodicInterval.PerfectFifth:
                    if curr_melodic_interval == next_melodic_interval:
                        if curr_voicing_interval.top_voice != next_voicing_interval.top_voice:
                            sub_result.update(voicing_interval, 'Parallel Fifth')

            results.append(sub_result.get_dict())

        return results
            