from fourparts import Voice, VoicingInterval
from fourparts.processes.containers.NoteContainer import NoteContainer


class DyadContainer(NoteContainer):
    """A container that stores notes when a dataframe of a midi file is processed.
    At every instance when there are four notes present, a VoicingInterval(Dyad) is created.
    """

    def __init__(self, bass, soprano):
        """Constructor method for DyadContainer

        Parameters
        ----------
        bass, soprano : int
        """

        self.container = {
            'Bass': bass,
            'Soprano': soprano
        }

    @classmethod
    def create_container(cls, notes):
        """Fills `container` given a list of notes in ascending order.

        Parameters
        ----------
        notes : list of notes
            Must strictly be a list of 2 notes sorted in ascending order.

        Returns
        -------
        DyadContainer

        Raises
        ------
        IndexError
            If `notes` does not have exactly 2 elements.
        """

        if len(notes) != 2:
            raise IndexError('Ensure 2 notes are passed in.')

        return cls(notes[0], notes[1])

    def update_note_on(self, note):
        return super().update_note_on(note)

    def update_note_off(self, note):
        return super().update_note_off(note)

    def create_music_structure(self):
        """Creates a VoicingInterval when container is filled.

        Returns
        -------
        VoicingInterval
        """

        return VoicingInterval.create_voicing_interval(Voice(self.container['Bass']),
                                                       Voice(self.container['Soprano']))
