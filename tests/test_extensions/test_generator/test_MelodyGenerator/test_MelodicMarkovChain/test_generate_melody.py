from fourparts import MelodyTrainer, MelodyGenerator, NoteProgression

import pytest


MARKOV_CHAIN = MelodyTrainer.create(["samples/chorale_F.mid"]).train()


def test():
    assert type(MelodyGenerator(MARKOV_CHAIN).generate_melody(5)) == NoteProgression


def test_exception():
    with pytest.raises(ValueError):
        assert MelodyGenerator(MARKOV_CHAIN).generate_melody(-1) is not None
