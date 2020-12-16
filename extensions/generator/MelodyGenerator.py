class MelodyTrainer:
    """Represents the class that constructs a Markov Chain based on an initial seed.

    Attributes
    ----------
    seed : list of NoteProgression
    """

    def __init__(self, seed):
        """Constructor method.

        Parameters
        ----------
        seed : list of NoteProgression
        """

        self.seed = seed

    @classmethod
    def create(cls, midi_seed):
        """Constructs a MelodyTrainer based on a list of midi files.

        Parameters
        ----------
        midi_seed : list of midi files

        Returns
        -------
        MelodyTrainer
        """
        pass
