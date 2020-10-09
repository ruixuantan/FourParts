from enum import Enum


class Scales(Enum):
    """Represents different scales.
    Currently, only major or minor scales are implemented.
    """

    Major = 'MAJOR'
    Minor = 'MINOR'

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

    @classmethod
    def create_scale_from_index(cls, scale):
        """Creates an instance of a Scale from the index.

        Parameters
        ----------
        scale : int
            Either 0 for major or 1 for minor.

        Returns
        -------
        Scale

        Raises
        ------
        ValueError
            If scale is not 0 or 1.
        """

        if scale == 0:
            return cls('MAJOR')
        elif scale == 1:
            return cls('MINOR')
        else:
            raise ValueError("Pass in only either 0 for major or 1 for minor.")

    @classmethod
    def get_scale_index(cls, scale):
        """Gets the index of the scale.

        Parameters
        ----------
        scale : Scales

        Returns
        -------
        int
            Either 0 for Major or 1 for Minor.

        Raises
        ------
        ValueError
            If scale does not exist.
        """

        if scale == Scales.Major:
            return 0
        elif scale == Scales.Minor:
            return 1
        else:
            raise ValueError("Scale input does not exist. Only major or minor scales are supported.")
