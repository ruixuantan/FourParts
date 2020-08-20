from fourparts import KeyClassifier, Key, Scales
import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy
import pytest


@pytest.fixture
def training_data():
    data = pd.read_csv("tests/test_analyser/test_KeyClassifier/train.csv")
    return data


@pytest.fixture
def key_classifier():
    model = LogisticRegression()
    return KeyClassifier(model)


def test_train(key_classifier, training_data):
    key_classifier.train(training_data)
    assert key_classifier.trained == True


def test_test_train(key_classifier, training_data):
    res = key_classifier.test_train(training_data)
    assert isinstance(res['Correct_Predictions'], int)
    assert isinstance(res['Total_Predictions'], int)
    assert isinstance(res['Accuracy'], float)
    assert isinstance(res['Results'], pd.DataFrame)
    assert key_classifier.trained == True
    

def test_predict(key_classifier, training_data):
    key_classifier.train(training_data)
    predict_data = {
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
    predicted = key_classifier.predict(predict_data)
    assert predicted is not None


def test_predict_midi(key_classifier, training_data):
   key_classifier.train(training_data)
   predicted = key_classifier.predict_midi("samples/chorale_F.mid")
   assert predicted is not None


def test_convert_to_key():
    test_cases = [
        [0, 1],
        [23]
    ]

    expected = [
        [Key('C', Scales.Major), Key('C', Scales.Minor)],
        [Key('B', Scales.Minor)]
    ] 

    for case, ex in zip(test_cases, expected):
        assert KeyClassifier.convert_to_key(case) == ex
        