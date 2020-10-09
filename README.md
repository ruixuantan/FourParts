# FourParts

[![Actions Status](https://github.com/ruixuantan/FourParts/workflows/Python%20Package%20CI/badge.svg)](https://github.com/ruixuantan/FourParts/actions)
[![codecov](https://codecov.io/gh/ruixuantan/FourParts/branch/master/graph/badge.svg)](https://codecov.io/gh/ruixuantan/FourParts)

A python package to analyse 4 part writing. \
Currently, it can only check for:
* Parallel fifths and octaves.
* Pitch Class Set.
* Melodic Intervals between 2 part writing.
* A KeyClassifier object that is able to identify the key of a midifile.

## Build Package
First, run:
```console
$ python setup.py bdist_wheel
```
This produces a file: `dist/fourparts-0.0.1-py3-none-any.whl` \
Then, run:
```console
$ pip install fourparts-0.0.1-py3-none-any.whl
```
This package can be imported via: `import fourparts`
## Demo
Configure demo.py to read the midi file required.
Then, run:
```console
$ python demo.py
```
Three .csv files of results will appear in the same directory as demo.py.
One of which is an analysis of a 2 part writing.

The midi files input should contain, strictly, either 2 or 4 parts at all times.
Overlaps in voices will be sorted in accordance to pitch and treated as SATB from there.

Configure `KeyClassifier_demo.py` to read in the training data and midifile input. Running `python KeyClassifier_demo.py` will print out the key of the midifile.

## How it works

### Chord/Dyad progression analyser
The midi file is converted to a csv file initially, using the py-midicsv library.
Then, the csv file will be parsed to generate a progression of chords or Dyads. A chord or dyad is formed whenever the corresponding number of notes are triggered. This progression will then be analysed: checked for parallel fifths and octaves, pitch class set, etc. If any 2 notes are static, it will not be parallel.