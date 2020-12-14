from fourparts import Dyad, PreProcessor
import pandas as pd
import pytest


def test_cases():
    # Dyads should be able to be instantiated with
    # Voice and its subtypes.
    return [
        (
            pd.read_csv("samples/chorale_G_2parts.csv"),
            [
                Dyad(43, 67),
                Dyad(55, 67),
                Dyad(52, 67),
                Dyad(50, 74),
                Dyad(52, 71),
                Dyad(42, 71),
                Dyad(42, 69),
                Dyad(43, 67),
                Dyad(47, 67),
                Dyad(45, 67),
                Dyad(45, 69),
                Dyad(43, 71),
                Dyad(50, 69),
            ],
        )
    ]


@pytest.mark.parametrize("df, expected", test_cases())
def test_eval(df, expected):
    assert PreProcessor(2).get_progression(df) == expected
