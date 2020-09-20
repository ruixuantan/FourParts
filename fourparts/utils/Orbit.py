class Orbit:
    """A class to represent a mathematical Orbit structure.

    Attributes
    ----------
    index : int
        The index of the current pointer to the Orbit.
    orbit : tuple of object
        The tuple of objects that are contained in the Orbit.
    """

    def __init__(self, orbit, index=0):
        """Constructor method of Orbit.
        
        Parameters
        ----------
        orbit: iterable
            The actual orbit.
        index : int
            The pointer towards the element in the orbit referred to.
        """

        if index >= len(orbit):
            raise IndexError("Ensure index is contained within the length of the orbit.")

        self.index = index
        self.orbit = tuple(orbit)

    def __str__(self):
        return "Index: {0}, Orbit: {1}".format(self.index, self.orbit.__str__())
        
    def curr_elem(self):
        """Method to get the current element of the Orbit.

        Returns
        -------
        object
        """

        return self.orbit[self.index]

    def _shift_clockwise(self):
        """Shifts the index clockwise by 1 unit.
        
        Returns
        -------
        None
        """

        self.index += 1
        if self.index == len(self.orbit):
            self.index = 0

    def _shift_counter_clockwise(self):
        """Shifts the index counter clockwise by 1 unit.

        Returns
        -------
        None
        """

        self.index -= 1
        if self.index == -1:
            self.index = len(self.orbit) - 1

    def shift_n(self, n):
        """Shifts the index by n steps.
        
        Parameters
        ----------
        n : int
            If n > 0, it is shifted clockwise.
            If n < 0, it is shifted counterclockwise.
        
        Returns
        -------
        object
            The element in the Orbit shifted into.
        """

        actual_shifts = n % len(self.orbit)

        for _ in range(actual_shifts):
            self._shift_clockwise()

        return self.curr_elem()

    def set_to_zero(self):
        """Set the index of the orbit to 0.

        Returns
        -------
        object
            The first element of the Orbit.
        """

        self.index = 0
        return self.curr_elem()
    
    def freeze(self):
        """Gets a list of the Orbit, with the starting element
        being the element the current index is pointing to.
        
        Returns
        -------
        list of object
        """

        output = []
        for i in range(self.index, len(self.orbit)):
            output.append(self.orbit[i])

        for i in range(self.index):
            output.append(self.orbit[i])

        return output
