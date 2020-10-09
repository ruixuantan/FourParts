from fourparts import Chord

import pytest


def test_cases():
    default_status = 'No parallel 5ths or 8ths'

    test_cases = [
        (
            Chord(0, 1, 2, 3), Chord(1, 2, 3, 4),
            {
                'BassTenor': default_status,
                'BassAlto': default_status,
                'BassSoprano': default_status,
                'TenorAlto': default_status,
                'TenorSoprano': default_status,
                'AltoSoprano': default_status
            }
        ),
        (
            Chord(0, 1, 2, 7), Chord(1, 2, 3, 8),
            {
                'BassTenor': default_status,
                'BassAlto': default_status,
                'BassSoprano': 'Parallel Fifth',
                'TenorAlto': default_status,
                'TenorSoprano': default_status,
                'AltoSoprano': default_status
            }
        ),
        (
            Chord(5, 10, 16, 22), Chord(6, 11, 17, 23),
            {
                'BassTenor': default_status,
                'BassAlto': default_status,
                'BassSoprano': default_status,
                'TenorAlto': default_status,
                'TenorSoprano': 'Parallel Octave',
                'AltoSoprano': default_status
            }
        ),
        (
            Chord(20, 27, 32, 36), Chord(8, 27, 32, 36),
            {
                'BassTenor': default_status,
                'BassAlto': default_status,
                'BassSoprano': default_status,
                'TenorAlto': default_status,
                'TenorSoprano': default_status,
                'AltoSoprano': default_status
            }
        )
    ]

    return test_cases


@pytest.mark.parametrize("chord_one, chord_two, result", test_cases())
def test_eval(chord_one, chord_two, result):
    generated_result = chord_one.check_parallel_intervals(chord_two)
    assert generated_result == result
