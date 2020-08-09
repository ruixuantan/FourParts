from fourparts.music_structures.Key import Key
from fourparts.music_structures.Scales import Scales
from fourparts.processes.NoteFrequencies import NoteFrequencies
from fourparts.processes.preprocess import midi_to_df

from sklearn.model_selection import train_test_split
import pandas as pd


def _parse_data(data):
    """
    Parameters
    ----------
    data : pandas.DataFrame
        Columns:
            Name: Name, dtype: str
                Name of the piece that has been analysed.
            Name: pitchcenter, dtype: str
                Pitchcenter of the piece, as in Notes.NOTES.
            Name: scale, dtype: str
                Either 'major' or 'minor'.
            Name: C, dtype: float
            Name: C#/Db, dtype: float
            Name: D, dtype: float
            Name: D#/Eb, dtype: float
            Name: E, dtype: float
            Name: F, dtype: float
            Name: F#/Gb, dtype: float
            Name: G, dtype: float
            Name: G#/Ab, dtype: float
            Name: A, dtype: float
            Name: A#/Bb, dtype: float
            Name: B, dtype: float
                percentages of the occurences of the note.

    Returns
    -------
    tuple of pd.DataFrame
        At index 0 is all the percentages of note frequencies.
        At index 1 is the keys (in index form).
    """

    # TODO: find method to create keys in place
    df_x = data.iloc[:, 3:]
    
    scale_list = list(data['scale'])
    for i in range(len(scale_list)):
        scale_list[i] = Scales.create_scale(scale_list[i])

    df_y = pd.Series(data=[Key(row['pitchcenter'], scale_list[i]).get_key_index()
                           for i, row in data.iterrows()],
                     name='keys')
    return df_x, df_y


class KeyClassifier:
    """A class to detect the key of a piece of music.
    Need not be four part writing.

    A machine learning model is trained using a dataset of
    keys (in index form) and its associated NoteFrequency percentages.

    Attributes
    ----------
    model : sklearn classifier model object
    trained : bool
        True if the model has been trained.
    """

    def __init__(self, classifier_model):
        """Constructor method to initialise the MLPClassifier

        Parameters
        ----------
        classifier_model : sklearn classifier model object
        """

        self.model = classifier_model
        self.train = False

    def _fit(self, x_train, y_train):
        """Training of neural network.
        Sets self.train to True.

        Parameters
        ----------
        x_train : numpy array of Keys
        y_train: numpy array of note frequency percentages
        """

        self.model.fit(x_train, y_train)
        self.train = True

    def train(self, data):
        """Actual training of the neural network.

        Parameters
        ----------
        data : pandas.DataFrame
            See _parse_data above.

        Returns
        -------
        self
        """

        df_x, df_y = _parse_data(data)
        self._fit(df_x, df_y)

        return self

    def test_train(self, data, test_size=0.2):
        """Testing of the neural network.

        Parameters
        ----------
        data : pandas.DataFrame
            See _parse_data above.
        test_size : float
            Between 0.0 and 1.0. Determines the ratio of test_samples to use.
            Default is 0.2.

        Returns
        -------
        str
            Results of the training set.
        """

        df_x, df_y = _parse_data(data)
        x_train, x_test, y_train, y_test = train_test_split(df_x,
                                                            df_y,
                                                            test_size=test_size)
        self._fit(x_train, y_train)

        count = 0
        predict = self.model.predict(x_test)
        total = len(predict)

        for i in range(total):
            if predict[i] == y_test.values[i]:
                count += 1
        
        accuracy = round(count / total * 100, 2)

        return '''
               Correct predictions: {0}
               Total predictions: {1}
               Percentage accuracy: {2}
               '''.format(count, total, accuracy)

    def predict(self, data):
        """Predicts the actual key of data.

        Parameters
        ----------
        data : dict of list of float
            Each element in the list should be a percentage.
            An example:
            {
                'C': [50.0],
                'C#/Db': [0],
                'D': [0],
                'D#/Eb': [50.0],
                'E': [0],
                'F': [0],
                'F#/Gb': [0],
                'G': [0],
                'G#/Ab': [0],
                'A': [0],
                'A#/Bb': [0],
                'B': [0]
            }

        Returns
        -------
        list of Key
        """

        if not self.train:
            raise AttributeError("KeyClassifier has not been trained.")
        return self.model.predict(pd.DataFrame(data))

    def predict_midi(self, midi_file):
        """Predicts the key of the given midi file.

        Parameters
        ----------
        midi_file : str
            Directory to the midi file.

        Returns
        -------
        list of Key
        """

        df = midi_to_df(midi_file)
        freq = NoteFrequencies.create_note_frequencies()
        freq.count(df)
        freq_percentage = freq.convert_to_percentage()

        data = {}
        # convert to a dict of list of float
        for key in freq_percentage.keys():
            data[key] = [freq_percentage[key]]

        return self.predict(data)

    @classmethod
    def convert_to_key(cls, index_list):
        """Given a list of key indexes, convert into a list of keys.

        Parameters
        ----------
        index_list : list of int (between 0 to 23)
            As generated from predict or predict_midi

        Returns
        -------
        list of Key
        """

        key_list = []
        for idx in index_list:
            key = Key.get_key_from_index(idx)
            key_list.append(key)

        return key_list
