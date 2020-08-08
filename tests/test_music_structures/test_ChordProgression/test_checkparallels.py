from fourparts import Chord, ChordProgression

import pytest


def test_cases():
    """
    Test cases:
    1. Standard Test
    2. Standard negative test
    3. Test of same chords but with change of notes in between.
       Should not incur parallels.

    """

    default_status = 'No parallel 5ths or 8ths'

    test_cases = [
        (
            [Chord(0, 1, 2, 3), Chord(1, 2, 3, 4)],
            [{
                'BassTenor': default_status,
                'BassAlto': default_status,
                'BassSoprano': default_status,
                'TenorAlto': default_status,
                'TenorSoprano': default_status,
                'AltoSoprano': default_status
            }]
        ),
        (
            [Chord(0, 1, 2, 7), Chord(1, 2, 3, 8), Chord(3, 4, 5, 6)],
            [
                {
                    'BassTenor': default_status,
                    'BassAlto': default_status,
                    'BassSoprano': 'Parallel Fifth',
                    'TenorAlto': default_status,
                    'TenorSoprano': default_status,
                    'AltoSoprano': default_status
                },
                {
                    'BassTenor': default_status,
                    'BassAlto': default_status,
                    'BassSoprano': default_status,
                    'TenorAlto': default_status,
                    'TenorSoprano': default_status,
                    'AltoSoprano': default_status
                }
            ]
        ),
        (
            [Chord(20, 27, 32, 36), Chord(8, 27, 32, 36)],
            [
                {
                    'BassTenor': default_status,
                    'BassAlto': default_status,
                    'BassSoprano': default_status,
                    'TenorAlto': default_status,
                    'TenorSoprano': default_status,
                    'AltoSoprano': default_status
                }
            ]
        )
    ]

    return test_cases


@pytest.mark.parametrize("chord_progression, results", test_cases())
def test_eval(chord_progression, results):
    generated_results = ChordProgression(chord_progression).check_parallels()
    assert generated_results == results
