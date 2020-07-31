class NoteEvent:
    """Represents a note-on or note-off event in a converted csv file.
        
    Attributes
    ----------
    note : int
    on : bool
        True for on, False for off.
    """

    def __init__(self, note, on):
        """
        Parameters
        ----------
        note : int
        on : bool
        """

        self.note = note
        self.on = on

    def __repr__(self):
        return "Note: {0}, On: {1}".format(self.note, self.on)
