from fourparts import Chord
from fourparts.structures.voices.Voice import BASS, TENOR, ALTO, SOPRANO
from fourparts.processes.containers.NoteContainer import NoteContainer


class ChordContainer(NoteContainer):
    """A container that stores notes when a dataframe of a midi file is processed.
    At every instance when there are four notes present, a Chord is created.

    Attributes
    ----------
    container : dict of notes
        Each value is set to None initially.
    """

    def __init__(self, bass, tenor, alto, soprano):
        """Constructor method.

        Parameters
        ----------
        bass, tenor, alto, soprano : int
        """

        self.container = {BASS: bass, TENOR: tenor, ALTO: alto, SOPRANO: soprano}

    @classmethod
    def create_container(cls, notes):
        """Fills `container` given a list of notes in ascending order.

        Parameters
        ----------
        notes : list of notes
            Must strictly be a list of 4 notes sorted in ascending order.

        Returns
        -------
        ChordContainer

        Raises
        ------
        IndexError
            If `notes` does not have exactly 4 elements.
        """

        if len(notes) != 4:
            raise IndexError("Ensure 4 notes are passed in notes.")

        return cls(notes[0], notes[1], notes[2], notes[3])

    def update_note_on(self, note):
        return super().update_note_on(note)

    def update_note_off(self, note):
        return super().update_note_off(note)

    def create_music_structure(self):
        """Creates a chord when container is filled.

        Returns
        -------
        Chord
        """

        return Chord(
            self.container[BASS],
            self.container[TENOR],
            self.container[ALTO],
            self.container[SOPRANO],
        )
