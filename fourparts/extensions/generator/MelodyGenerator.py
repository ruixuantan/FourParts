import random
from fourparts.processes.PreProcessor import midi_to_df
from fourparts.processes.MelodyExtractor import MelodyExtractor
from fourparts.structures.progressions.NoteProgression import NoteProgression


class MelodicMarkovChain:
    """Represents a Markov Chain for melodies.

    Attributes
    ----------
    markov_chain : dict
        Keys of `Notes`. Values of dict.
        Sub dict has keys of `Notes` and values of int.
        For example:
        {
            Notes(4): { Notes(3): 2, Notes(1): 1 },
            Notes(5): { Notes(2): 3, Notes(1): 2 }
            ...
        }
    """

    def __init__(self, markov_chain):
        """Constructor method.

        Parameters
        ----------
        markov_chain : list of list of int
        """

        self.markov_chain = markov_chain

    def __eq__(self, other):
        return (
            self.__class__ == other.__class__
            and self.markov_chain == other.markov_chain
        )

    def __repr__(self):
        return self.markov_chain

    @classmethod
    def initialise(cls):
        """Generates an empty Markov Chain.

        Returns
        -------
        MelodicMarkovChain
        """

        return cls({})

    def update(self, key, value):
        """Updates the markov chain.

        Parameters
        ----------
        key : Notes
        value : Notes
        """

        if key not in self.markov_chain:
            self.markov_chain[key] = {}

        if value not in self.markov_chain[key]:
            self.markov_chain[key][value] = 0

        assert value in self.markov_chain[key]
        self.markov_chain[key][value] += 1

    def random_select_note(self, note):
        """Gets a random note based on the markov chain.
        Must have percentages calculated.

        Parameters
        ----------
        note : Notes

        Returns
        -------
        Notes
        """

        if note not in self.markov_chain:
            return random.choice(list(self.markov_chain.keys()))

        return random.choices(
            list(self.markov_chain[note].keys()), list(self.markov_chain[note].values())
        )[0]

    def random_walk(self, length):
        """Gets a list of random notes based on the markov chain.

        Parameters
        ----------
        length : int
            length of the progression

        Returns
        -------
        NoteProgression

        Raises
        ------
        ValueError
            If length is not more than 0
        """

        if length <= 0:
            raise ValueError("Length must be more than 0.")

        next_note = random.choice(list(self.markov_chain.keys()))
        notes_list = [next_note]

        for _ in range(length):
            next_note = self.random_select_note(next_note)
            notes_list.append(next_note)

        return NoteProgression(notes_list)


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
    def _midi_to_melody(cls, midi_file):
        """Converts midi_file to melody.

        Returns
        -------
        NoteProgression
        """

        df = midi_to_df(midi_file, save=False)
        return MelodyExtractor.get_melody(df)

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

        seed = [MelodyTrainer._midi_to_melody(midi_file) for midi_file in midi_seed]
        return cls(seed)

    def train(self):
        """Generates the melodic markov chain, based on `seed`.

        Returns
        -------
        MelodicMarkovChain
        """

        trained_markov_chain = MelodicMarkovChain.initialise()
        for progression in self.seed:
            for i in range(len(progression) - 1):
                curr_note = progression[i]
                next_note = progression[i + 1]
                trained_markov_chain.update(curr_note, next_note)

        # To complete the markov chain
        trained_markov_chain.update(progression[-1], progression[0])

        return trained_markov_chain


class MelodyGenerator:
    """Represents class that generates the melody.

    Attributes
    ----------
    melodic_markov_chain : MelodicMarkovChain
    """

    def __init__(self, melodic_markov_chain):
        """Constructor method.

        Parameters
        ----------
        melodic_markov_chain : MelodicMarkovChain
            It has to be trained and have percentages calculated.
        """
        self.markov_chain = melodic_markov_chain

    def generate_melody(self, length):
        """Generates the melody.

        Parameters
        ----------
        length : int
            Length of the generated NoteProgression.

        Returns
        -------
        NoteProgression

        Raises
        ------
        ValueError
            If length is not more than 0.
        """

        if length <= 0:
            raise ValueError("Length must be more than 0.")

        return self.markov_chain.random_walk(length)


if __name__ == "__main__":
    markov_chain = MelodyTrainer.create(["samples/chorale_F.mid"]).train()
    print(MelodyGenerator(markov_chain).generate_melody(5))
