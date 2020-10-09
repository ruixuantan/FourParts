from fourparts.commons.Orbit import Orbit
import pytest


def test_cases():
    orbit_1 = [1, 2, 3]
    orbit_2 = ('X', 'Y', 'Z', 'T')

    test_cases = [
        ([1], 0, [1]),
        (orbit_1, 0, [1, 2, 3]),
        (orbit_1, 1, [2, 3, 1]),
        (orbit_2, 3, ['T', 'X', 'Y', 'Z'])
    ]

    return test_cases


@pytest.mark.parametrize("orbit, index, expected", test_cases())
def test_eval(orbit, index, expected):
    assert Orbit(orbit, index).get_curr_orbit() == expected
