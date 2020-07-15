"""A Chord is made up of 4 notes."""

from fourparts.music_structures.Voice import *
from fourparts.music_structures.MelodicInterval import MelodicInterval
from fourparts.music_structures.VoicingInterval import *
from fourparts.music_structures.PitchClassSet.PitchClassSet import PitchClassSet


INTERVALS = ('BassTenor', 'BassAlto', '')

class Chord:

    def __init__(self, bass, tenor, alto, soprano):
        """Constructor class for chord.

        Attributes
        ----------
        bass, tenor, alto, soprano : int
        """

        self.bass = Bass(bass)
        self.tenor = Tenor(tenor)
        self.alto = Alto(alto)
        self.soprano = Soprano(soprano)

    def __str__(self):
        return 'Bass: {0}, Tenor: {1}, Alto: {2}, Soprano: {3}' \
                .format(self.bass, self.tenor, self.alto, self.soprano)

    def __eq__(self, other):
        if not isinstance(other, Chord):
            return False
        
        return self.bass == other.bass and \
               self.tenor == other.tenor and \
               self.alto == other.alto and \
               self.soprano == other.soprano

    def get_intervals(self):
        """Generates a dictionary of intervals of the chord.

        Returns
        -------
        dict of VoicingInterval
        """

        intervals = {}

        intervals['BassTenor'] = BassTenor.create_voicing_interval(self.bass, self.tenor)
        intervals['BassAlto'] = BassAlto.create_voicing_interval(self.bass, self.alto)
        intervals['BassSoprano'] = BassSoprano.create_voicing_interval(self.bass, self.soprano)
        intervals['TenorAlto'] = TenorAlto.create_voicing_interval(self.tenor, self.alto)
        intervals['TenorSoprano'] = TenorSoprano.create_voicing_interval(self.tenor, self.soprano)
        intervals['AltoSoprano'] = AltoSoprano.create_voicing_interval(self.alto, self.soprano)

        return intervals

    def check_parallel_intervals(self, other):
        """Generates a dictionary of results, indicating
        if the specified interval is a parallel 5th or 8th.

        Returns
        -------
        dict of str
            Indicates only either a parallel 5th or 8th
        """

        self_intervals = self.get_intervals()
        other_intervals = other.get_intervals()

        default_status = 'No parallel 5ths or 8ths'

        result = {
            'BassTenor': default_status,
            'BassAlto': default_status,
            'BassSoprano': default_status,
            'TenorAlto': default_status,
            'TenorSoprano': default_status,
            'AltoSoprano': default_status
        }

        for interval in result.keys():
            self_voicing_interval = self_intervals[interval]
            other_voicing_interval = other_intervals[interval]

            if self_voicing_interval.is_parallel_octave(other_voicing_interval):
                result[interval] = 'Parallel Octave'

            elif self_voicing_interval.is_parallel_fifth(other_voicing_interval):
                result[interval] = 'Parallel Fifth'

        return result

    def get_pitch_class_set(self):
        """Generates the associated PitchClassSet.

        Returns
        -------
        PitchClassSet
        """

        pitch_class_set = PitchClassSet.create_pitch_class_set([
            self.bass.note,
            self.tenor.note,
            self.alto.note,
            self.soprano.note])

        return pitch_class_set
