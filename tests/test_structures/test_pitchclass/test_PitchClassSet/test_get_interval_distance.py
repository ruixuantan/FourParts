from fourparts.structures.pitchclass.PitchClassSet import get_interval_distances
from fourparts.commons.Orbit import Orbit

import pytest


def test_cases():

    return [
        (Orbit([0]), []),
        (Orbit([0, 5]), [5]),
        (Orbit([0, 4, 7]), [7, 4]),
        (Orbit([3, 6, 9, 0]), [9, 6, 3]),
        (Orbit([10, 0, 2]), [4, 2]),
    ]


@pytest.mark.parametrize("pitches, expected_distances", test_cases())
def test_eval(pitches, expected_distances):
    assert get_interval_distances(pitches) == expected_distances
