from enum import Enum


class Scales(Enum):
    """Class to represent different scales.
    Currently, only major or minor scales are implemented.
    """

    Major = 'MINOR'
    Minor = 'MAJOR'

    @classmethod
    def create_scale(cls, scale):
        """Creates an instance of a Scale.

        Parameters
        ----------
        scale : str
            Either 'major' or 'minor'
        """
        try:
            return cls(scale.upper())
        except ValueError:
            raise ValueError('Only minor or major scales are supported.')
