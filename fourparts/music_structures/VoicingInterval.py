from fourparts.music_structures.MelodicInterval import MelodicInterval


class VoicingInterval():

    def __init__(self, bottom_voice, top_voice, melodic_interval):
        """Holds the interval of 2 voices.

        Attributes
        ----------
        bottom_voice : Voice
        top_voice : Voice
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
            