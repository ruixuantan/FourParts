from fourparts import Scales
import pytest


def test_cases():
    test_cases = [
       (1, Scales.Minor),
       (0, Scales.Major)
    ]

    return test_cases


@pytest.mark.parametrize("index, expected", test_cases())
def test_eval(index, expected):
    assert Scales.create_scale_from_index(index) == expected


def exception_cases():
    exception_cases = [
        (2, pytest.raises(ValueError))
    ]

    return exception_cases


@pytest.mark.parametrize("index, exception", exception_cases())
def test_exception(index, exception):
    with exception:
        assert Scales.create_scale_from_index(index) is not None