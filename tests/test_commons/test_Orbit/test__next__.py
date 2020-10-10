from fourparts.commons.Orbit import Orbit
import pytest


def test_cases():
    orbit_1 = Orbit((1, 2, 3))
    orbit_2 = Orbit(('X', 'Y', 'Z', 'T'), 1)

    # note that testing is mutable
    return [
        (orbit_1, [1, 2, 3]),
        (orbit_2, ['Y', 'Z', 'T', 'X'])
    ]


@pytest.mark.parametrize("orbit, expected", test_cases())
def test_eval(orbit, expected):
    for elem, expected_elem in zip(orbit, expected):
        assert elem == expected_elem
