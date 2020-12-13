from fourparts import Notes, NoteProgression, ToneRow


TONEROW = ToneRow(NoteProgression([
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

TONEROW_RETROGRADE = ToneRow(NoteProgression([
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

TONEROW_INVERSE = ToneRow(NoteProgression([
    Notes(9),
    Notes(4),
    Notes(7),
    Notes(2),
    Notes(1),
    Notes(11),
    Notes(0),
    Notes(10),
    Notes(5),
    Notes(8),
    Notes(3),
    Notes(6)
]))

TONEROW_RETROGRADE_INVERSE = ToneRow(NoteProgression([
    Notes(6),
    Notes(3),
    Notes(8),
    Notes(5),
    Notes(10),
    Notes(0),
    Notes(11),
    Notes(1),
    Notes(2),
    Notes(7),
    Notes(4),
    Notes(9)
]))

#
# TONEROW_STANDARD = ToneRow(NoteProgression([
#     Notes(21),
#     Notes(2),
#     Notes(11),
#     Notes(40),
#     Notes(5),
#     Notes(0),
#     Notes(19),
#     Notes(6),
#     Notes(8),
#     Notes(25),
#     Notes(34),
#     Notes(3)
# ]))
