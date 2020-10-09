from fourparts import Scales, Key
import pytest


def test_cases():
    test_cases = [
        ('C', Scales.Major, 0),
        ('C', Scales.Minor, 1),
        ("C#/Db", Scales.Major, 2),
        ("C#/Db", Scales.Minor, 3),
        ("D", Scales.Major, 4),
        ("D", Scales.Minor, 5),
        ('D#/Eb', Scales.Major, 6),
        ('D#/Eb', Scales.Minor, 7),
        ('E', Scales.Major, 8),
        ('E', Scales.Minor, 9),
        ('F', Scales.Major, 10),
        ('F', Scales.Minor, 11),
        ('F#/Gb', Scales.Major, 12),
        ('F#/Gb', Scales.Minor, 13),
        ('G', Scales.Major, 14),
        ('G', Scales.Minor, 15),
        ('G#/Ab', Scales.Major, 16),
        ('G#/Ab', Scales.Minor, 17),
        ('A', Scales.Major, 18),
        ('A', Scales.Minor, 19),
        ('A#/Bb', Scales.Major, 20),
        ('A#/Bb', Scales.Minor, 21),
        ('B', Scales.Major, 22),
        ('B', Scales.Minor, 23)
    ]

    return test_cases


@pytest.mark.parametrize("pitchcenter, scale, index", test_cases())
def test_eval(pitchcenter, scale, index):
    key = Key(pitchcenter, scale)
    assert Key.get_key_from_index(index) == key
