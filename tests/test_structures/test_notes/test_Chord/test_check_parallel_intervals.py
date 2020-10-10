from fourparts import Chord
from fourparts.structures.notes.Chord import (
    BASS_TENOR,
    BASS_ALTO,
    BASS_SOPRANO,
    TENOR_ALTO,
    TENOR_SOPRANO,
    ALTO_SOPRANO,
    PARALLEL_DEFAULT,
    PARALLEL_FIFTH,
    PARALLEL_OCTAVE
)

import pytest


def test_cases():
    return [
        (
            Chord(0, 1, 2, 3), Chord(1, 2, 3, 4),
            {
                BASS_TENOR: PARALLEL_DEFAULT,
                BASS_ALTO: PARALLEL_DEFAULT,
                BASS_SOPRANO: PARALLEL_DEFAULT,
                TENOR_ALTO: PARALLEL_DEFAULT,
                TENOR_SOPRANO: PARALLEL_DEFAULT,
                ALTO_SOPRANO: PARALLEL_DEFAULT
            }
        ),
        (
            Chord(0, 1, 2, 7), Chord(1, 2, 3, 8),
            {
                BASS_TENOR: PARALLEL_DEFAULT,
                BASS_ALTO: PARALLEL_DEFAULT,
                BASS_SOPRANO: PARALLEL_FIFTH,
                TENOR_ALTO: PARALLEL_DEFAULT,
                TENOR_SOPRANO: PARALLEL_DEFAULT,
                ALTO_SOPRANO: PARALLEL_DEFAULT
            }
        ),
        (
            Chord(5, 10, 16, 22), Chord(6, 11, 17, 23),
            {
                BASS_TENOR: PARALLEL_DEFAULT,
                BASS_ALTO: PARALLEL_DEFAULT,
                BASS_SOPRANO: PARALLEL_DEFAULT,
                TENOR_ALTO: PARALLEL_DEFAULT,
                TENOR_SOPRANO: PARALLEL_OCTAVE,
                ALTO_SOPRANO: PARALLEL_DEFAULT
            }
        ),
        (
            Chord(20, 27, 32, 36), Chord(8, 27, 32, 36),
            {
                BASS_TENOR: PARALLEL_DEFAULT,
                BASS_ALTO: PARALLEL_DEFAULT,
                BASS_SOPRANO: PARALLEL_DEFAULT,
                TENOR_ALTO: PARALLEL_DEFAULT,
                TENOR_SOPRANO: PARALLEL_DEFAULT,
                ALTO_SOPRANO: PARALLEL_DEFAULT
            }
        )
    ]


@pytest.mark.parametrize("chord_one, chord_two, result", test_cases())
def test_eval(chord_one, chord_two, result):
    generated_result = chord_one.check_parallel_intervals(chord_two)
    assert generated_result == result
