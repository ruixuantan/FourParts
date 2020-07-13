"""A Chord is made up of 4 notes."""

from fourparts.music_structures.Voice import *
from fourparts.music_structures.MelodicInterval import MelodicInterval
from fourparts.music_structures.VoicingInterval import *
from fourparts.music_structures.PitchClassSet.PitchClassSet import PitchClassSet


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
