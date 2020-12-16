from fourparts import MelodicMarkovChain, Notes

import pytest


def test_cases():
    return [
        ({Notes(3): {Notes(1): 1}}, Notes(3), Notes(1), {Notes(3): {Notes(1): 2}}),
        (
            {Notes(3): {Notes(1): 1}},
            Notes(3),
            Notes(2),
            {Notes(3): {Notes(1): 1, Notes(2): 1}},
        ),
        ({}, Notes(3), Notes(1), {Notes(3): {Notes(1): 1}}),
    ]


@pytest.mark.parametrize("markov_chain, key, value, expected", test_cases())
def test_eval(markov_chain, key, value, expected):
    actual_markov_chain = MelodicMarkovChain(markov_chain)
    actual_markov_chain.update(key, value)
    assert actual_markov_chain == MelodicMarkovChain(expected)
