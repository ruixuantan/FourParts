from fourparts import Notes, NoteProgression, ToneRow


TONEROW_IN_OCTAVE = ToneRow(NoteProgression([
    Notes(9),
    Notes(2),
    Notes(11),
    Notes(4),
    Notes(5),
    Notes(7),
    Notes(6),
    Notes(8),
    Notes(1),
    Notes(10),
    Notes(3),
    Notes(0)
]))

TONEROW_IN_OCTAVE_RETROGRADE = ToneRow(NoteProgression([
    Notes(0),
    Notes(3),
    Notes(10),
    Notes(1),
    Notes(8),
    Notes(6),
    Notes(7),
    Notes(5),
    Notes(4),
    Notes(11),
    Notes(2),
    Notes(9)
]))

TONEROW_STANDARD = ToneRow(NoteProgression([
    Notes(21),
    Notes(2),
    Notes(11),
    Notes(40),
    Notes(5),
    Notes(0),
    Notes(19),
    Notes(6),
    Notes(8),
    Notes(25),
    Notes(34),
    Notes(3)
]))

TONEROW_STANDARD_RETROGRADE = ToneRow(NoteProgression([
    Notes(3),
    Notes(34),
    Notes(25),
    Notes(8),
    Notes(6),
    Notes(19),
    Notes(0),
    Notes(5),
    Notes(40),
    Notes(11),
    Notes(2),
    Notes(21)
]))