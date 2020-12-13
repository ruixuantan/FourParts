from fourparts import Notes, NoteProgression, ToneRow


TONEROW_IN_OCTAVE = ToneRow(NoteProgression([
    Notes.create_note(9),
    Notes.create_note(2),
    Notes.create_note(11),
    Notes.create_note(4),
    Notes.create_note(5),
    Notes.create_note(7),
    Notes.create_note(6),
    Notes.create_note(8),
    Notes.create_note(1),
    Notes.create_note(10),
    Notes.create_note(3),
    Notes.create_note(0)
]))

TONEROW_IN_OCTAVE_RETROGRADE = ToneRow(NoteProgression([
    Notes.create_note(0),
    Notes.create_note(3),
    Notes.create_note(10),
    Notes.create_note(1),
    Notes.create_note(8),
    Notes.create_note(6),
    Notes.create_note(7),
    Notes.create_note(5),
    Notes.create_note(4),
    Notes.create_note(11),
    Notes.create_note(2),
    Notes.create_note(9)
]))

TONEROW_STANDARD = ToneRow(NoteProgression([
    Notes.create_note(21),
    Notes.create_note(2),
    Notes.create_note(11),
    Notes.create_note(40),
    Notes.create_note(5),
    Notes.create_note(0),
    Notes.create_note(19),
    Notes.create_note(6),
    Notes.create_note(8),
    Notes.create_note(25),
    Notes.create_note(34),
    Notes.create_note(3)
]))

TONEROW_STANDARD_RETROGRADE = ToneRow(NoteProgression([
    Notes.create_note(3),
    Notes.create_note(34),
    Notes.create_note(25),
    Notes.create_note(8),
    Notes.create_note(6),
    Notes.create_note(19),
    Notes.create_note(0),
    Notes.create_note(5),
    Notes.create_note(40),
    Notes.create_note(11),
    Notes.create_note(2),
    Notes.create_note(21)
]))