from fourparts import PitchClassSet

import pytest


def test_cases():
    """
    Test cases:
    1. Tests an already normalised set.
    2. Tests a transposition.
    3-5. Test inversions.

    """

    test_cases = [
        ([0, 1, 3], (0, 1, 3)),
        ([1, 2, 4], (0, 1, 3)),
        ([0, 2, 10], (0, 2, 4)),
        ([0, 5, 7], (0, 2, 7)),
        ([0, 5, 9], (0, 4, 7)),
        ([0, 4, 7, 10], (0, 3, 6, 8))
    ]

    return test_cases


@pytest.mark.parametrize("pitches, results", test_cases())
def test_eval(pitches, results):
    assert results == PitchClassSet.normalise(pitches)


def exception_cases():
    test_cases = [
        ([0], pytest.raises(Exception)),
    ]

    return test_cases


@pytest.mark.parametrize("pitches, exception", exception_cases())
def test_exceptions(pitches, exception):
    with exception:
        assert PitchClassSet.normalise(pitches) is not None
