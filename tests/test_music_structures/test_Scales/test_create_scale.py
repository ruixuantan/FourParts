from fourparts import Scales
import pytest


def test_cases():
    test_cases = [
       ('mInOr', Scales.Minor),
       ('major', Scales.Major)
    ]

    return test_cases


@pytest.mark.parametrize("scale, expected", test_cases())
def test_eval(scale, expected):
    assert Scales.create_scale(scale) == expected


def exception_cases():
    exception_cases = [
        ('not a scale', pytest.raises(ValueError))
    ]

    return exception_cases


@pytest.mark.parametrize("scale, exception", exception_cases())
def test_exception(scale, exception):
    with exception:
        assert Scales.create_scale(scale) is not None