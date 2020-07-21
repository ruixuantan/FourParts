from fourparts import Chord


class NoteContainer:
    """A container that stores notes when a dataframe of a midi file is processed.
    At every instance when there are four notes present, a Chord is created.

    Attributes
    ----------
    container : dict of notes
        Each value is set to None initially.
    """

    def __init__(self, bass, tenor, alto, soprano):
        """Constructor method for NoteContainer

        Parameters
        ----------
        bass, tenor, alto, soprano : int
        """

        self.container = { 
            'Bass': bass, 
            'Tenor': tenor, 
            'Alto': alto, 
            'Soprano': soprano
        }

    @classmethod
    def create_container(cls, notes):
        """Given a list of notes in ascending order, fills `container`.

        Parameters
        ----------
        notes : list of notes
            Must strictly be a list of 4 notes sorted in ascending order.
            Exception will be thrown in Chord.

        Returns
        -------
        NoteContainer

        Raises
        ------
        Exception
            If notes does not have exactly 4 elements.
        """

        if len(notes) != 4:
            raise Exception('Ensure 4 notes are passed in notes.')

        return cls(notes[0], notes[1], notes[2], notes[3])

    def update_note_on(self, note):
        """Starting from Bass, inserts `note` into 
        the first empty key. If the container is full, returns a Chord.

        Parameters
        ----------
        note : int

        Returns
        -------
        Chord
            Only returns when all values of container are not None.
        """

        for key in self.container.keys():
            if self.container[key] is None:
                self.container[key] = note
                break

        if all(self.container.values()):
            chord = self.create_chord()
            return chord

        return None

    def update_note_off(self, note):
        """Starting from Bass, checks if `note` equals
        any of its values. If equal, it changes the value to None.

        Parameters
        ----------
        note : int
        """

        for key in self.container.keys():
            if self.container[key] == note:
                self.container[key] = None

    def create_chord(self):
        """Creates a chord when container is filled.

        Returns
        -------
        Chord
        """

        return Chord(self.container['Bass'],
                    self.container['Tenor'],
                    self.container['Alto'],
                    self.container['Soprano'])
