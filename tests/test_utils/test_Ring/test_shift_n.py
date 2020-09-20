from fourparts.utils.Ring import Ring
import pytest


def test_cases():
    ring_1 = Ring((1, 2, 3)) 
    ring_2 = Ring(('X', 'Y', 'Z', 'T'))

    # note that testing is mutable
    test_cases = [
       (ring_1, -2, 2),
       (ring_1, 3, 2),
       (ring_1, 0, 2),
       (ring_2, 0, 'X'),
       (ring_2, 7, 'T'),
       (ring_2, -8, 'T')
    ]

    return test_cases


@pytest.mark.parametrize("ring, n, expected", test_cases())
def test_eval(ring, n, expected):
    assert ring.shift_n(n) == expected
