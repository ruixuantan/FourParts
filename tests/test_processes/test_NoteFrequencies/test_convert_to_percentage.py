from fourparts import NoteFrequencies
import pytest


def test_cases():
    return [
        (
            {'C': 1, 'C#/Db': 1, 'D': 1, 'D#/Eb': 0, 'E': 0, 'F': 0, 'F#/Gb': 0,
             'G': 0, 'G#/Ab': 0, 'A': 0, 'A#/Bb': 0, 'B': 0},
            {'C': 33.33, 'C#/Db': 33.33, 'D': 33.33, 'D#/Eb': 0, 'E': 0, 'F': 0, 'F#/Gb': 0,
             'G': 0, 'G#/Ab': 0, 'A': 0, 'A#/Bb': 0, 'B': 0}
        ),
        (
            {'C': 3, 'C#/Db': 0, 'D': 0, 'D#/Eb': 0, 'E': 0, 'F': 3, 'F#/Gb': 0,
             'G': 0, 'G#/Ab': 0, 'A': 0, 'A#/Bb': 0, 'B': 0},
            {'C': 50.00, 'C#/Db': 0, 'D': 0, 'D#/Eb': 0, 'E': 0, 'F': 50.00, 'F#/Gb': 0,
             'G': 0, 'G#/Ab': 0, 'A': 0, 'A#/Bb': 0, 'B': 0}
        ),
        (
            {'C': 0, 'C#/Db': 0, 'D': 0, 'D#/Eb': 0, 'E': 0, 'F': 0, 'F#/Gb': 0,
             'G': 0, 'G#/Ab': 0, 'A': 0, 'A#/Bb': 0, 'B': 0},
            {'C': 0, 'C#/Db': 0, 'D': 0, 'D#/Eb': 0, 'E': 0, 'F': 0, 'F#/Gb': 0,
             'G': 0, 'G#/Ab': 0, 'A': 0, 'A#/Bb': 0, 'B': 0}
        )
    ]


@pytest.mark.parametrize("count, expected", test_cases())
def test_eval(count, expected):
    assert NoteFrequencies(count).convert_to_percentage() == expected


def exception_cases():
    return [
        (
            {'C': 3, 'C#/Db': 0, 'D': 0, 'D#/Eb': 0, 'E': 0, 'F': 3, 'F#/Gb': 0,
             'G': 0, 'G#/Ab': 0, 'A': 0, 'A#/Bb': 0, 'B': 0},
            -1,
            pytest.raises(ValueError)
        )
    ]


@pytest.mark.parametrize("count, dp, exception", exception_cases())
def test_exception(count, dp, exception):
    with exception:
        assert NoteFrequencies(count).convert_to_percentage(dp=dp) is not None
