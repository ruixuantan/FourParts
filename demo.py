import fourparts as fp
import pandas as pd


# file_name = 'chorale_F'

# df = fp.midi_to_df('samples/' + file_name + '.mid')
# chords = fp.get_chord_progression(df)
# chord_progression = fp.ChordProgression(chords)

# # gets pitch class sets
# pitch_class_sets = chord_progression.get_pitch_class_sets()
# pd.DataFrame(pitch_class_sets).to_csv(file_name + '_pitch_class_sets.csv')

# # check parallels
# result = chord_progression.check_parallels()
# pd.DataFrame(result).to_csv(file_name + '_parallel_results.csv')

filename = 'chorale_G_2parts'
df = fp.midi_to_df('samples/' + filename + '.mid')
df.to_csv('test.csv')