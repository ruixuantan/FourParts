from fourparts.music_structures.PitchClassSet.PitchClassSet import get_interval_distances
from fourparts.utils.Orbit import Orbit

import pytest


def test_cases():

    test_cases = [
        (Orbit([0]), []),
        (Orbit([0, 5]), [5]),
        (Orbit([0, 4, 7]), [7, 4]), 
        (Orbit([3, 6, 9, 0]), [9, 6, 3]),
        (Orbit([10, 0, 2]), [4, 2])
    ]

    return test_cases


@pytest.mark.parametrize("pitches, expected_distances", test_cases())
def test_eval(pitches, expected_distances):
    print(get_interval_distances(pitches))
    assert get_interval_distances(pitches) == expected_distances