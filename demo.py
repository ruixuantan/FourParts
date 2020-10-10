import fourparts as fp
import pandas as pd


file_name = 'chorale_F'

df = fp.midi_to_df('samples/' + file_name + '.mid', save=True)
chords = fp.PreProcessor(4).get_progression(df)
chord_progression = fp.ChordProgression(chords)

# gets pitch class sets
pitch_class_sets = chord_progression.get_pitch_class_sets()
pd.DataFrame(pitch_class_sets).to_csv(file_name + '_pitch_class_sets.csv')

# check parallels
result = chord_progression.check_parallels()
pd.DataFrame(result).to_csv(file_name + '_parallel_results.csv')


# demonstration for 2 parts
file_name = 'chorale_G_2parts'

df = fp.midi_to_df('samples/' + file_name + '.mid', save=True)
dyads = fp.PreProcessor(2).get_progression(df)
dyad_progression = fp.DyadProgression(dyads)

# gets intervals between each dyad
dyad_intervals = dyad_progression.get_harmonic_intervals()
pd.DataFrame(dyad_intervals).to_csv(file_name + '_dyad_intervals.csv')
