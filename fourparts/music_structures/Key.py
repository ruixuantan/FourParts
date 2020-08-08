from fourparts.music_structures.Notes import Notes
from fourparts.music_structures.Scales import Scales


class Key:
    """Class to define all 24 keys.
    """

    KEYS = {
        Notes.NOTES[0]: {
            Scales.Major: 'C_MAJOR',
            Scales.Minor: 'C_MINOR'
        },
        Notes.NOTES[1]: {
            Scales.Major: 'C#/Db_MAJOR',
            Scales.Minor: 'C#/Db_MINOR'
        },
        Notes.NOTES[2]: {
            Scales.Major: 'D_MAJOR',
            Scales.Minor: 'D_MINOR'
        },
        Notes.NOTES[3]: {
            Scales.Major: 'D#/Eb_MAJOR',
            Scales.Minor: 'D#/Eb_MINOR'
        },
        Notes.NOTES[4]: {
            Scales.Major: 'E_MAJOR',
            Scales.Minor: 'E_MINOR'
        },
        Notes.NOTES[5]: {
            Scales.Major: 'F_MAJOR',
            Scales.Minor: 'F_MINOR'
        },
        Notes.NOTES[6]: {
            Scales.Major: 'F#/Gb_MAJOR',
            Scales.Minor: 'F#/Gb_MINOR'
        },
        Notes.NOTES[7]: {
            Scales.Major: 'G_MAJOR',
            Scales.Minor: 'G_MINOR'
        },
        Notes.NOTES[8]: {
            Scales.Major: 'G#/Gb_MAJOR',
            Scales.Minor: 'G#/Ab_MINOR'
        },
        Notes.NOTES[9]: {
            Scales.Major: 'A_MAJOR',
            Scales.Minor: 'A_MINOR'
        },
        Notes.NOTES[10]: {
            Scales.Major: 'A#/Bb_MAJOR',
            Scales.Minor: 'A#/Bb_MINOR'
        },
        Notes.NOTES[11]: {
            Scales.Major: 'B_MAJOR',
            Scales.Minor: 'B_MINOR'
        }
    }

    def __init__(self, key):
        """Constructor method of Key.

        Parameters
        ----------
        key : str
            One of the 24 keys in KEYS.
        """

        self.key = key

    def __str__(self):
        return self.key

    @classmethod
    def create_scale(cls, pitchcenter, scale):
        """Factory method of Scale.

        Parameters
        ----------
        pitchcenter : str
            A note as represented in Notes.NOTES.
        key : Scales
            Either Scales.Major or Scales.Minor.
        """

        return cls(Key.KEYS[pitchcenter][scale])
