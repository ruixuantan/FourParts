class Voice:
    """A class that represents the type of voice.

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
        return isinstance(other, Voice) and \
               self.note == other.note

    def __str__(self):
        return str(self.note)


class Soprano(Voice):

    def __init__(self, note):
        super().__init__(note)


class Alto(Voice):

    def __init__(self, note):
        super().__init__(note)


class Tenor(Voice):

    def __init__(self, note):
        super().__init__(note)


class Bass(Voice):

    def __init__(self, note):
        super().__init__(note)
