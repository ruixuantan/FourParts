from fourparts import MelodyTrainer


def test():
    """For now, just check if all notes generated are contained within the MarkovChain.
    Update if necessary.
    """

    markov_chain = MelodyTrainer.create(["samples/chorale_F.mid"]).train()
    note_progression = markov_chain.random_walk(5)
    for note in note_progression:
        print(note)
        print(markov_chain.markov_chain)
        assert note in markov_chain.markov_chain
