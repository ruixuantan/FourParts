from midiutil import MIDIFile


class MidiWriter:
    """A class to write fourpart chords.

    Attributes
    ----------
    midi : MIDIFile
    """

    TRACKS = 2
    CHANNEL = 0
    # bpm
    TEMPO = 60
    VOLUME = 100
    # number of beats for a note
    DURATION = 1

    def __init__(self):
        """Initialises the number of tracks, initial time and tempo.
        """
        self.midi = MIDIFile(MidiWriter.TRACKS)
        # arguments are track, time, tempo
        self.midi.addTempo(0, 0, MidiWriter.TEMPO)

    def add_pitches(self, track, pitches, time):
        """Adds the pitches into the midifile.

        Parameters
        ----------
        track : int
            The track where the note is to be inserted into.
        pitches : list of int
            The pitches that are to be added to the midi file.
        time : int
            The time when the first note event is to occur.
            Measured in beats
        
        Returns
        -------
        self
        """

        for i, pitch in enumerate(pitches):
            self.midi.addNote(track,
                              MidiWriter.CHANNEL,
                              pitch,
                              time + i,
                              MidiWriter.DURATION,
                              MidiWriter.VOLUME)
        return self

    def add_chords(self, chord_progression):
        """Turn a chord progression into a midifile.

        Parameters
        ----------
        chord_progression : ChordProgression

        Returns
        -------
        self
        """

        bass_pitches = []
        tenor_pitches = []
        alto_pitches = []
        soprano_pitches = []

        for chord in chord_progression.progression:
            bass_pitches.append(chord.bass.note)
            tenor_pitches.append(chord.tenor.note)
            alto_pitches.append(chord.alto.note)
            soprano_pitches.append(chord.soprano.note)

        self.add_pitches(1, bass_pitches, 0)
        self.add_pitches(1, tenor_pitches, 0)
        self.add_pitches(0, alto_pitches, 0)
        self.add_pitches(0, soprano_pitches, 0)

        return self

    def save_midi(self, filename="midifile.mid"):
        """Converts midi object to actual midi file.

        Parameters
        ----------
        filename : str
            Must end with with a '.mid' suffix.
            Default is given as 'midifile.mid'.

        Raises
        ------
        Exception
            If `filename` does not end with '.mid'.
        """

        if filename[-4:] != '.mid':
            raise Exception("{} does not end with '.mid'.".format(filename))

        with open(filename, "wb") as output_file:
            self.midi.writeFile(output_file)
