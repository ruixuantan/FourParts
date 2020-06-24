"""Represents a note-on or note-off event in a converted csv file.
"""

class NoteEvent:

    def __init__(self, note, on):
        """
        Attributes
        ----------
        note : int
        on : bool
            True for on, False for off.
        """

        self.note = note
        self.on = on
