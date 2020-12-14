from fourparts.exceptions.NoteOrderException import NoteOrderException
from fourparts.structures.voices.Voice import Bass, Tenor, Alto, Soprano
from fourparts.structures.voices.VoicingInterval import (
    BassTenor,
    BassAlto,
    BassSoprano,
    TenorAlto,
    TenorSoprano,
    AltoSoprano,
    BASS_TENOR,
    BASS_ALTO,
    BASS_SOPRANO,
    TENOR_ALTO,
    TENOR_SOPRANO,
    ALTO_SOPRANO,
)
from fourparts.structures.pitchclass.PitchClassSet import PitchClassSet


PARALLEL_DEFAULT = "No Parallels"
PARALLEL_FIFTH = "Parallel Fifth"
PARALLEL_OCTAVE = "Parallel Octave"


class Chord:
    """A collection of 4 Voices, sorted in ascending order.

    Attributes
    ----------
    bass, tenor, alto, soprano : Voice
    """

    def __init__(self, bass, tenor, alto, soprano):
        """Constructor method.

        Parameters
        ----------
        bass, tenor, alto, soprano : int

        Raises
        ------
        NoteOrderException
            If order of notes input is wrong.
        """

        if not bass <= tenor <= alto <= soprano:
            raise NoteOrderException("Notes are out of order.")

        self.bass = Bass(bass)
        self.tenor = Tenor(tenor)
        self.alto = Alto(alto)
        self.soprano = Soprano(soprano)

    def __str__(self):
        return "Bass: {0}, Tenor: {1}, Alto: {2}, Soprano: {3}".format(
            self.bass, self.tenor, self.alto, self.soprano
        )

    def __eq__(self, other):
        if not isinstance(other, Chord):
            return False

        return (
            self.bass == other.bass
            and self.tenor == other.tenor
            and self.alto == other.alto
            and self.soprano == other.soprano
        )

    def get_intervals(self):
        """Generates a dictionary of intervals of the chord.

        Returns
        -------
        dict of VoicingInterval
        """

        return {
            BASS_TENOR: BassTenor.create_voicing_interval(self.bass, self.tenor),
            BASS_ALTO: BassAlto.create_voicing_interval(self.bass, self.alto),
            BASS_SOPRANO: BassSoprano.create_voicing_interval(self.bass, self.soprano),
            TENOR_ALTO: TenorAlto.create_voicing_interval(self.tenor, self.alto),
            TENOR_SOPRANO: TenorSoprano.create_voicing_interval(
                self.tenor, self.soprano
            ),
            ALTO_SOPRANO: AltoSoprano.create_voicing_interval(self.alto, self.soprano),
        }

    def check_parallel_intervals(self, other):
        """Generates a dictionary of results, indicating
        if the specified interval is a parallel 5th or 8th.

        Parameters
        ----------
        other : Chord

        Returns
        -------
        dict of str
            Indicates only either a parallel 5th or 8th
        """

        self_intervals = self.get_intervals()
        other_intervals = other.get_intervals()

        result = {
            BASS_TENOR: PARALLEL_DEFAULT,
            BASS_ALTO: PARALLEL_DEFAULT,
            BASS_SOPRANO: PARALLEL_DEFAULT,
            TENOR_ALTO: PARALLEL_DEFAULT,
            TENOR_SOPRANO: PARALLEL_DEFAULT,
            ALTO_SOPRANO: PARALLEL_DEFAULT,
        }

        for interval in result.keys():
            self_voicing_interval = self_intervals[interval]
            other_voicing_interval = other_intervals[interval]

            if self_voicing_interval.is_parallel_octave(other_voicing_interval):
                result[interval] = PARALLEL_OCTAVE

            elif self_voicing_interval.is_parallel_fifth(other_voicing_interval):
                result[interval] = PARALLEL_FIFTH

        return result

    def get_pitch_class_set(self):
        """Generates the associated PitchClassSet.

        Returns
        -------
        PitchClassSet
        """

        pitch_class_set = PitchClassSet.create_pitch_class_set(
            self.bass.note, self.tenor.note, self.alto.note, self.soprano.note
        )

        return pitch_class_set
