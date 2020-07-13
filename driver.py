import fourparts as fp

import json
import pandas as pd


file_name = 'chorale_F'

df = fp.midi_to_df('samples/' + file_name + '.mid')
chords = fp.get_chord_progression(df)
chord_progression = fp.ChordProgression(chords)
result = chord_progression.check_parallels()
pd.DataFrame(result).to_csv(file_name + '_results.csv')
for c in chord_progression.progression:
    print(c.get_pitch_class_set())