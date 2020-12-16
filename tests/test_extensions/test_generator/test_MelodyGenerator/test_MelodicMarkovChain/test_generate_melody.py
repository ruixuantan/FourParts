from fourparts import MelodyTrainer, MelodyGenerator, NoteProgression
from tests.samples import CHORALE_F_MIDI
import pytest


MARKOV_CHAIN = MelodyTrainer.create([CHORALE_F_MIDI]).train()


def test():
    assert type(MelodyGenerator(MARKOV_CHAIN).generate_melody(5)) == NoteProgression


def test_exception():
    with pytest.raises(ValueError):
        assert MelodyGenerator(MARKOV_CHAIN).generate_melody(-1) is not None
