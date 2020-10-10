from fourparts.commons.Orbit import Orbit
import pytest


def test_cases():
    orbit_1 = Orbit((1, 2, 3))
    orbit_2 = Orbit(('X', 'Y', 'Z', 'T'))

    # note that testing is mutable
    return [
        (orbit_1, -2, 2),
        (orbit_1, 3, 2),
        (orbit_1, 0, 2),
        (orbit_2, 0, 'X'),
        (orbit_2, 7, 'T'),
        (orbit_2, -8, 'T')
    ]


@pytest.mark.parametrize("orbit, n, expected", test_cases())
def test_eval(orbit, n, expected):
    assert orbit.shift(n) == expected
