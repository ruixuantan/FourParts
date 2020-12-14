BASS = "Bass"
TENOR = "Tenor"
ALTO = "Alto"
SOPRANO = "Soprano"


class Voice:
    """Represents the type of voice.

    Attributes
    ----------
    note : int
        The note of the voice.
    """

    def __init__(self, note):
        """Constructor method.

        Parameters
        ----------
        note : int
            The note of the voice.
        """

        self.note = note

    def __eq__(self, other):
        return isinstance(other, Voice) and self.note == other.note

    def __str__(self):
        return str(self.note)

    def get_voice_name(self):
        """Gets the name of the class.

        Returns
        -------
        """

        pass


class Soprano(Voice):
    def __init__(self, note):
        super().__init__(note)

    def get_voice_name(self):
        return SOPRANO


class Alto(Voice):
    def __init__(self, note):
        super().__init__(note)

    def get_voice_name(self):
        return ALTO


class Tenor(Voice):
    def __init__(self, note):
        super().__init__(note)

    def get_voice_name(self):
        return TENOR


class Bass(Voice):
    def __init__(self, note):
        super().__init__(note)

    def get_voice_name(self):
        return BASS
