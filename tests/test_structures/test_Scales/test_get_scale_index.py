from fourparts import Scales
import pytest


def test_cases():
    return [
        (Scales.Major, 0),
        (Scales.Minor, 1),
    ]


@pytest.mark.parametrize("scale, expected", test_cases())
def test_eval(scale, expected):
    assert Scales.get_scale_index(scale) == expected


def exception_cases():
    return [
        ('wrong type', pytest.raises(ValueError))
    ]


@pytest.mark.parametrize("scale, exception", exception_cases())
def test_exception(scale, exception):
    with exception:
        assert Scales.get_scale_index(scale) is not None
