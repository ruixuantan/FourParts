from fourparts import Chord, ChordProgression
from fourparts.structures.notes.Chord import (
    BASS_TENOR,
    BASS_ALTO,
    BASS_SOPRANO,
    TENOR_ALTO,
    TENOR_SOPRANO,
    ALTO_SOPRANO,
    PARALLEL_DEFAULT,
    PARALLEL_FIFTH,
)

import pytest


def test_cases():
    """
    Test cases:
    1. Standard Test
    2. Standard negative test
    3. Test of same chords but with change of notes in between.
       Should not incur parallels.
    """

    return [
        (
            [Chord(0, 1, 2, 3), Chord(1, 2, 3, 4)],
            [
                {
                    BASS_TENOR: PARALLEL_DEFAULT,
                    BASS_ALTO: PARALLEL_DEFAULT,
                    BASS_SOPRANO: PARALLEL_DEFAULT,
                    TENOR_ALTO: PARALLEL_DEFAULT,
                    TENOR_SOPRANO: PARALLEL_DEFAULT,
                    ALTO_SOPRANO: PARALLEL_DEFAULT,
                }
            ],
        ),
        (
            [Chord(0, 1, 2, 7), Chord(1, 2, 3, 8), Chord(3, 4, 5, 6)],
            [
                {
                    BASS_TENOR: PARALLEL_DEFAULT,
                    BASS_ALTO: PARALLEL_DEFAULT,
                    BASS_SOPRANO: PARALLEL_FIFTH,
                    TENOR_ALTO: PARALLEL_DEFAULT,
                    TENOR_SOPRANO: PARALLEL_DEFAULT,
                    ALTO_SOPRANO: PARALLEL_DEFAULT,
                },
                {
                    BASS_TENOR: PARALLEL_DEFAULT,
                    BASS_ALTO: PARALLEL_DEFAULT,
                    BASS_SOPRANO: PARALLEL_DEFAULT,
                    TENOR_ALTO: PARALLEL_DEFAULT,
                    TENOR_SOPRANO: PARALLEL_DEFAULT,
                    ALTO_SOPRANO: PARALLEL_DEFAULT,
                },
            ],
        ),
        (
            [Chord(20, 27, 32, 36), Chord(8, 27, 32, 36)],
            [
                {
                    BASS_TENOR: PARALLEL_DEFAULT,
                    BASS_ALTO: PARALLEL_DEFAULT,
                    BASS_SOPRANO: PARALLEL_DEFAULT,
                    TENOR_ALTO: PARALLEL_DEFAULT,
                    TENOR_SOPRANO: PARALLEL_DEFAULT,
                    ALTO_SOPRANO: PARALLEL_DEFAULT,
                }
            ],
        ),
    ]


@pytest.mark.parametrize("chord_progression, results", test_cases())
def test_eval(chord_progression, results):
    generated_results = ChordProgression(chord_progression).check_parallels()
    assert generated_results == results
