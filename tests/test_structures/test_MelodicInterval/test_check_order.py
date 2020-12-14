from fourparts import Order

import pytest


def test_cases():

    return [
        (70, 70, Order.Static),
        (50, 55, Order.Ascending),
        (1, 0, Order.Descending),
    ]


@pytest.mark.parametrize("bottom_note_int, top_note_int, expected", test_cases())
def test_eval(bottom_note_int, top_note_int, expected):
    assert Order.check_order(bottom_note_int, top_note_int) == expected
