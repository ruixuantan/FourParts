from fourparts import MelodicMarkovChain, Notes

import pytest


def test_cases():
    return [
        (
            {
                Notes(3): {Notes(1): 1}
            },
            {
                Notes(3): {Notes(1): 1}
            }
        ),
        (
            {
                Notes(3): {Notes(1): 1, Notes(2): 3}
            },
            {
                Notes(3): {Notes(1): 0.25, Notes(2): 0.75}
            }
        ),
    ]


@pytest.mark.parametrize("markov_chain, expected", test_cases())
def test_eval(markov_chain, expected):
    actual_markov_chain = MelodicMarkovChain(markov_chain)
    actual_markov_chain.calculate_percentages()
    assert actual_markov_chain == MelodicMarkovChain(expected)
