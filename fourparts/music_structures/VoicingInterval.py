from fourparts.music_structures.MelodicInterval import MelodicInterval


class VoicingInterval():
    """Holds the interval of 2 voices, along with the melodic interval
    between them.

    Attributes
    ----------
    bottom_voice : Voice
    top_voice : Voice
    melodic_interval : MelodicInterval
    """

    def __init__(self, bottom_voice, top_voice, melodic_interval):
        """Constructor for VoicingInterval.

        Parameters
        ----------
        bottom_voice : Voice
        top_voice : Voice
        melodic_interval : MelodicInterval
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
            raise Exception("Top note must be greater or equal to Bottom note.")
        else:
            interval = MelodicInterval.get_melodic_interval(bottom_note, top_note)
            return cls(bottom_voice, top_voice, interval)

    def _is_parallel(self, other):
        """Private method to check if 2 successive VoicingIntervals are
        parallel and not static.

        Parameters
        ----------
        other : VoicingInterval
        
        Returns
        -------
        boolean
            True if the VoicingIntervals are parallel and not static.
        """

        if self.top_voice.__class__.__name__ != other.top_voice.__class__.__name__ or \
           self.bottom_voice.__class__.__name__ != other.bottom_voice.__class__.__name__:
            raise Exception("Top and Bottom voices must be the same")
        
        return self.melodic_interval == other.melodic_interval and \
               self.top_voice != other.top_voice

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

        if self.melodic_interval == MelodicInterval.PerfectFifth:
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

        if self.melodic_interval == MelodicInterval.Octave:
            return self._is_parallel(other)

        return False


class BassTenor(VoicingInterval):

    def __init__(self, bottom_voice, top_voice, melodic_interval):
        super().__init__(bottom_voice, top_voice, melodic_interval)


class BassAlto(VoicingInterval):

    def __init__(self, bottom_voice, top_voice, melodic_interval):
        super().__init__(bottom_voice, top_voice, melodic_interval)


class BassSoprano(VoicingInterval):

    def __init__(self, bottom_voice, top_voice, melodic_interval):
        super().__init__(bottom_voice, top_voice, melodic_interval)


class TenorAlto(VoicingInterval):

    def __init__(self, bottom_voice, top_voice, melodic_interval):
        super().__init__(bottom_voice, top_voice, melodic_interval)


class TenorSoprano(VoicingInterval):

    def __init__(self, bottom_voice, top_voice, melodic_interval):
        super().__init__(bottom_voice, top_voice, melodic_interval)


class AltoSoprano(VoicingInterval):

    def __init__(self, bottom_voice, top_voice, melodic_interval):
        super().__init__(bottom_voice, top_voice, melodic_interval)
