from tests.test_structures.test_progression.test_ToneRow.tone_row_samples import (
    TONEROW, TONEROW_INVERSE
)

import pytest


def test_cases():
    return [
        (TONEROW, TONEROW_INVERSE)
    ]


@pytest.mark.parametrize("tone_row, expected", test_cases())
def test_eval(tone_row, expected):
    assert tone_row.get_inverse() == expected
