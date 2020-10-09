from abc import ABC, abstractmethod


class NoteContainer(ABC):
    """A container that stores notes when a dataframe of a midi file is processed.
    At every instance when there are n notes present, a nth music_structure is created.
    Currently, only VoicingInterval and Chord are implemented.

    Attributes
    ----------
    container : dict of notes
        Each value is set to None initially.
    """

    @classmethod
    def create_container(cls, notes):
        """Fills `container` given a list of notes in ascending order.

        Parameters
        ----------
        notes : list of notes
            Must strictly be a list of n notes sorted in ascending order.

        Returns
        -------
        NoteContainer

        Raises
        ------
        IndexError
            If notes does not have exactly n elements.
        """

        pass

    def __repr__(self):
        return str(self.container)

    def _sort_notes(self):
        """Sort notes in `container` to ascending order.
        """

        notes = list(self.container.values())
        notes.sort()
        for i, key in enumerate(self.container):
            self.container[key] = notes[i]

    @abstractmethod
    def update_note_on(self, note):
        """Starting from the lowest voice, inserts `note` into the first empty key.
        If the container is full, returns the associated music structure.

        Parameters
        ----------
        note : int

        Returns
        -------
        Music Stucture
            Only returns when all values of container are not None.
        """

        for key in self.container.keys():
            if self.container[key] is None:
                self.container[key] = note
                break

        if all(self.container.values()):
            self._sort_notes()
            music_structure = self.create_music_structure()
            return music_structure

        return None

    @abstractmethod
    def update_note_off(self, note):
        """Starting from Bass, checks if `note` equals
        any of its values. If equal, it changes the value to None.

        Parameters
        ----------
        note : int

        Returns
        -------
        bool
            Returns True if update is successful.
        """

        for key in self.container.keys():
            if self.container[key] == note:
                self.container[key] = None
                return True

        return False

    @abstractmethod
    def create_music_structure(self):
        """Creates the associated music structure when container is filled.

        Returns
        -------
        Music Stucture
        """

        pass
