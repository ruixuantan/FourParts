from fourparts.exceptions.NoteOrderException import NoteOrderException
from fourparts.structures.MelodicInterval import Interval


class VoicingInterval:
    """Holds the interval of 2 voices, along with the melodic interval
    between them.

    Attributes
    ----------
    bottom_voice : Voice
    top_voice : Voice
    melodic_interval : Interval
    """

    def __init__(self, bottom_voice, top_voice, melodic_interval):
        """Constructor method.

        Parameters
        ----------
        bottom_voice : Voice
        top_voice : Voice
        melodic_interval : Interval
        """

        self.bottom_voice = bottom_voice
        self.top_voice = top_voice
        self.melodic_interval = melodic_interval

    @classmethod
    def create_voicing_interval(cls, bottom_voice, top_voice):
        """Factory constructor method for VoicingInterval.

        Parameters
        ----------
        bottom_voice : Voice
        top_voice : Voice

        Returns
        -------
        VoicingInterval
        """

        top_note = top_voice.note
        bottom_note = bottom_voice.note

        if bottom_note > top_note:
            raise NoteOrderException(
                "Top note must be greater or equal to bottom note."
            )

        interval = Interval.get_interval(bottom_note, top_note)
        return cls(bottom_voice, top_voice, interval)

    def __str__(self):
        return "Bottom Voice: {0}, Top Voice: {1}, Interval: {2}".format(
            self.bottom_voice, self.top_voice, self.melodic_interval
        )

    def __eq__(self, other):
        return (
            isinstance(other, VoicingInterval)
            and self.bottom_voice == other.bottom_voice
            and self.top_voice == other.top_voice
            and self.melodic_interval == other.melodic_interval
        )

    def _is_parallel(self, other):
        """Checks if 2 successive VoicingIntervals are
        parallel and not static.

        Parameters
        ----------
        other : VoicingInterval

        Returns
        -------
        boolean
            True if the VoicingIntervals are parallel and not static.

        Raises
        ------
        TypeError
            If the top voice and bottom voice are of different types (different voices).
        """

        if (
            self.top_voice.get_voice_name() != other.top_voice.get_voice_name()
            or self.bottom_voice.get_voice_name() != other.bottom_voice.get_voice_name()
        ):
            raise TypeError("Top and Bottom voices must be of the same type.")

        return (
            self.melodic_interval == other.melodic_interval
            and self.top_voice != other.top_voice
        )

    def is_parallel_fifth(self, other):
        """Checks if 2 successive VoicingIntervals are
        a parallel 5th apart.

        Parameters
        ----------
        other : VoicingInterval

        Returns
        -------
        boolean
            True if the VoicingIntervals are a parallel 5th apart.
        """

        if self.melodic_interval == Interval.PerfectFifth:
            return self._is_parallel(other)

        return False

    def is_parallel_octave(self, other):
        """Checks if 2 successive VoicingIntervals are
        a parallel octave apart.

        Parameters
        ----------
        other : VoicingInterval

        Returns
        -------
        boolean
            True if the VoicingIntervals are a parallel octave apart.
        """

        if self.melodic_interval == Interval.Octave:
            return self._is_parallel(other)

        return False

    def get_voicing_interval_name(self):
        """Gets the name of the voicing interval.

        Returns
        -------
        str
        """

        pass


BASS_TENOR = "BassTenor"
BASS_ALTO = "BassAlto"
BASS_SOPRANO = "BassSoprano"
TENOR_ALTO = "TenorAlto"
TENOR_SOPRANO = "TenorSoprano"
ALTO_SOPRANO = "AltoSoprano"


class BassTenor(VoicingInterval):
    def __init__(self, bottom_voice, top_voice, melodic_interval):
        super().__init__(bottom_voice, top_voice, melodic_interval)

    @classmethod
    def get_voicing_interval_name(cls):
        return BASS_TENOR


class BassAlto(VoicingInterval):
    def __init__(self, bottom_voice, top_voice, melodic_interval):
        super().__init__(bottom_voice, top_voice, melodic_interval)

    @classmethod
    def get_voicing_interval_name(cls):
        return BASS_ALTO


class BassSoprano(VoicingInterval):
    def __init__(self, bottom_voice, top_voice, melodic_interval):
        super().__init__(bottom_voice, top_voice, melodic_interval)

    @classmethod
    def get_voicing_interval_name(cls):
        return BASS_SOPRANO


class TenorAlto(VoicingInterval):
    def __init__(self, bottom_voice, top_voice, melodic_interval):
        super().__init__(bottom_voice, top_voice, melodic_interval)

    @classmethod
    def get_voicing_interval_name(cls):
        return TENOR_ALTO


class TenorSoprano(VoicingInterval):
    def __init__(self, bottom_voice, top_voice, melodic_interval):
        super().__init__(bottom_voice, top_voice, melodic_interval)

    @classmethod
    def get_voicing_interval_name(cls):
        return TENOR_SOPRANO


class AltoSoprano(VoicingInterval):
    def __init__(self, bottom_voice, top_voice, melodic_interval):
        super().__init__(bottom_voice, top_voice, melodic_interval)

    @classmethod
    def get_voicing_interval_name(cls):
        return ALTO_SOPRANO
