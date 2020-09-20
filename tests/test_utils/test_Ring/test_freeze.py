from fourparts.utils.Ring import Ring
import pytest


def test_cases():
    ring_1 = (1, 2, 3)
    ring_2 = ('X', 'Y', 'Z', 'T')

    test_cases = [
       (ring_1, 0, [1, 2, 3]),
       (ring_1, 1, [2, 3, 1]),
       (ring_2, 3, ['T', 'X', 'Y', 'Z'])
    ]

    return test_cases


@pytest.mark.parametrize("ring, index, expected", test_cases())
def test_eval(ring, index, expected):
    assert Ring(ring, index).freeze() == expected
