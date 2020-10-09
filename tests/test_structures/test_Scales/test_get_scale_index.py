from fourparts import Scales
import pytest


def test_cases():
    test_cases = [
        (Scales.Major, 0),
        (Scales.Minor, 1),
    ]

    return test_cases


@pytest.mark.parametrize("scale, expected", test_cases())
def test_eval(scale, expected):
    assert Scales.get_scale_index(scale) == expected


def exception_cases():
    exception_cases = [
        ('wrong type', pytest.raises(ValueError))
    ]

    return exception_cases


@pytest.mark.parametrize("scale, exception", exception_cases())
def test_exception(scale, exception):
    with exception:
        assert Scales.get_scale_index(scale) is not None
