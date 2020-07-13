# FourParts #

A python package to analyse 4 part writing. \
Currently, it can only check for:
* parallel fifths and octaves.
* Pitch Class Set.

## Build Package ##
First, run:
```console
$ python setup.py bdist_wheel
```
This produces a file: `dist/fourparts_rxtan-0.0.1-py3-none-any.whl` \
Then, run:
```console
$ pip install fourparts_rxtan-0.0.1-py3-none-any.whl
```
This package can be imported via: `import fourparts`
## Demo ##
Configure driver.py to read the midi file required.
Then, run:
```console
$ python driver.py
```
A .csv file of results will appear in the same directory as driver.py.

This midi file should contain, strictly, 4 parts at all times.
Overlaps in voices will be sorted in accordance to pitch and treated as SATB from there.

## How it works ##
The midi file is converted to a csv file initially, using the py-midicsv library.
Then, the csv file will be parsed to generate a ChordProgression. Each chord is formed whenever four notes are triggered. This progression will then be checked for parallel fifths and octaves. If any 2 notes are static, it will not be parallel.