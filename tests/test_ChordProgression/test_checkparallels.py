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

    test_cases = [
        (
            [Chord(0, 1, 2, 3), Chord(1, 2, 3, 4)],
            [{
                'BassTenor': 'Correct',
                'BassAlto': 'Correct',
                'BassSoprano': 'Correct',
                'TenorAlto': 'Correct',
                'TenorSoprano': 'Correct',
                'AltoSoprano': 'Correct'
            }]
        ),
        (
            [Chord(0, 1, 2, 7), Chord(1, 2, 3, 8), Chord(3, 4, 5, 6)],
            [
                {
                    'BassTenor': 'Correct',
                    'BassAlto': 'Correct',
                    'BassSoprano': 'Parallel Fifth',
                    'TenorAlto': 'Correct',
                    'TenorSoprano': 'Correct',
                    'AltoSoprano': 'Correct'
                },
                {
                    'BassTenor': 'Correct',
                    'BassAlto': 'Correct',
                    'BassSoprano': 'Correct',
                    'TenorAlto': 'Correct',
                    'TenorSoprano': 'Correct',
                    'AltoSoprano': 'Correct'
                }
            ]
        ),
        (
            [Chord(20, 27, 32, 36), Chord(8, 27, 32, 36)],
            [
                {
                    'BassTenor': 'Correct',
                    'BassAlto': 'Correct',
                    'BassSoprano': 'Correct',
                    'TenorAlto': 'Correct',
                    'TenorSoprano': 'Correct',
                    'AltoSoprano': 'Correct'
                }
            ]
        )
    ]

    return test_cases


@pytest.mark.parametrize("chord_progression, results", test_cases())
def test_eval(chord_progression, results):
    generated_results = ChordProgression(chord_progression).check_parallels()
    assert generated_results == results
