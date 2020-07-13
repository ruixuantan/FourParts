import fourparts as fp

import json
import pandas as pd


file_name = 'chorale_F'

df = fp.midi_to_df('samples/' + file_name + '.mid')
chords = fp.get_chord_progression(df)
result = fp.ChordProgression(chords).check_parallels()
pd.DataFrame(result).to_csv(file_name + '_results.csv')