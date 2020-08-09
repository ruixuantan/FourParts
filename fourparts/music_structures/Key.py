from fourparts.music_structures.Notes import Notes
from fourparts.music_structures.Scales import Scales


class Key:
    """Class to define all 24 keys.

    Attributes
    ----------
    key : str
        As represented in KEYS
    pitchcenter : str
        One of the 12 notes in Notes.NOTES.
    scale : Scales
        Either Scales.Major or Scales.Minor
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

    def __init__(self, pitchcenter, scale):
        """Constructor method of Key.

        Parameters
        ----------
        pitchcenter : str
            One of the 12 notes in Notes.NOTES.
        scale : Scales
            Either Scales.Major or Scales.Minor
        """

        self.key = Key.KEYS[pitchcenter][scale]
        self.pitchcenter = pitchcenter
        self.scale = scale

    def __str__(self):
        return self.key

    def __eq__(self, other):
        return self.key == other.key

    def get_key_index(self):
        """Maps the key to its associated index.

        Returns
        -------
        int
            An int from 0 to 23s.
        """

        index = Notes.get_note_index(self.pitchcenter) * 2
        index += Scales.get_scale_index(self.scale)
        return index

    @classmethod
    def get_key_from_index(cls, index):
        """Maps the index back to a Key object.

        Parameters
        ----------
        index : int
            An int from 0 to 23.

        Returns
        -------
        Key
        """

        scale_index = index % 2
        # perform an int division
        pitchcenter_index = (index - scale_index) // 2

        return cls(Notes.create_note(pitchcenter_index),
                   Scales.create_scale_from_index(scale_index))
