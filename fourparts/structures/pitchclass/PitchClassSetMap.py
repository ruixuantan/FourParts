NOT_NAMED = "Not Named"

PITCH_CLASS_SET_MAP = (
    {
        (): "Empty Set"
    },
    {
        (0,): "Unison"
    },
    {
        (0, 1): "Semitone",
        (0, 2): "Tone",
        (0, 3): "Minor 3rd",
        (0, 4): "Major 3rd",
        (0, 5): "Perfect 4th",
        (0, 6): "Tritone",
        (0, 7): "Perfect 5th",
        (0, 8): "Minor 6th",
        (0, 9): "Major 6th",
        (0, 10): "Minor 7th",
        (0, 11): "Major 7th"
    },
    {
        (0, 1, 6): "Viennese trichord",
        (0, 2, 6): "Italian 6th",
        (0, 2, 7): "Suspended",
        (0, 3, 6): "Diminished",
        (0, 3, 7): "Minor",
        (0, 4, 7): "Major",
        (0, 4, 8): "Augmented"
    },
    {
        (0, 1, 4, 8): "Minor Major 7th",
        (0, 1, 5, 8): "Major 7th",
        (0, 2, 4, 8): "Augmented 7th",
        (0, 2, 5, 7): "Quartal",
        (0, 2, 5, 8): "Half Diminished 7th",
        (0, 2, 6, 8): "French 6th",
        (0, 3, 6, 8): "Dominant 7th",
        (0, 3, 6, 9): "Diminished 7th"
    },
    {
        (0, 2, 4, 6, 9): "Dominant 9th",
        (0, 2, 4, 7, 9): "Major Pentatonic Scale"
    },
    {
        (0, 1, 3, 5, 6, 8): "Major Eleventh",
        (0, 2, 3, 6, 8, 9): "Petrushka Chord",
        (0, 2, 4, 6, 8, 10): "Whole Tone"
    }
)
