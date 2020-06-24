"""A class to hold the analysed results between 2 chords.
It determines if there are either parallel fifths or octaves
between the given intervals.
"""

import json


class Result:

    def __init__(self):
        """Constructor method.

        Attributes
        ----------
        result : dict of str
            Contains all intervals and is initiliased to all 'Correct's.
        """

        self.result = {
            'BassTenor': 'Correct',
            'BassAlto': 'Correct',
            'BassSoprano': 'Correct',
            'TenorAlto': 'Correct',
            'TenorSoprano': 'Correct',
            'AltoSoprano': 'Correct'
        }

    def __str__(self):
        return str(self.result)

    def get_dict(self):
        return self.result

    def update(self, interval, status):
        """To update results if anything of significance is detected.

        Parameters
        ----------
        interval : str
            The interval in `self.results` to be updated.
        status : str
            The status to be changed to.

        Raises
        ------
        Exception
            If `interval` is not a valid input.
        """

        try:
            self.result[interval] = status
        except KeyError:
            raise Exception('''Input a valid interval string,
                            one of: bass_tenor, bass_alto, bass_soprano,
                            tenor_alto, tenor_soprano, alto_soprano''')
