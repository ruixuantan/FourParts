from fourparts import Bass, Soprano, VoicingInterval


class DyadContainer:
    """A container that stores Dyads.
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
        """Given a list of notes in ascending order, fills `container`.

        Parameters
        ----------
        notes : list of notes
            Must strictly be a list of 2 notes sorted in ascending order.

        Returns
        -------
        DyadContainer

        Raises
        ------
        Exception
            If notes does not have exactly 2 elements.
        """

        if len(notes) != 2:
            raise Exception('Ensure 2 notes are passed in.')

        return cls(notes[0], notes[1])

    def update_note_on(self, note):
        """Inserts `note` into bass. If bass is already occupied, insert into soprano.
        If the container is full, returns a VoicingInterval.

        Parameters
        ----------
        note : int

        Returns
        -------
        VoicingInterval
            Only returns when all values of container are not None.
        """

        for key in self.container.keys():
            if self.container[key] is None:
                self.container[key] = note
                break

        if all(self.container.values()):
            voicing_interval = self.create_dyad()
            return voicing_interval

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
                return None

    def create_dyad(self):
        """Creates a VoicingInterval when container is filled.

        Returns
        -------
        VoicingInterval
        """

        return VoicingInterval.create_voicing_interval(Bass(self.container['Bass']),
                                                       Soprano(self.container['Soprano']))
