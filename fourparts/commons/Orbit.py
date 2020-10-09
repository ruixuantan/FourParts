class Orbit:
    """Represent a mathematical Orbit structure.

    Attributes
    ----------
    orbit : tuple of object
        The tuple of objects that are contained in the Orbit.
    index : int
        The index of the current pointer to the Orbit.
    current : int
        To allow Orbit to be iterable.
    high : int
        To allow Orbit to be iterable. It is also the order/length of the orbit.
    """

    def __init__(self, orbit, index=0):
        """Constructor method.
        
        Parameters
        ----------
        orbit: iterable
            The actual orbit.
        index : int
            The pointer towards the element in the orbit referred to.
        """

        if index >= len(orbit):
            raise IndexError("Ensure index is contained within the length of the orbit.")
        
        self.orbit = tuple(orbit)
        self.index = index
        self.current = -1
        self.high = len(orbit)

    def __str__(self):
        return "Index: {0}, Orbit: {1}".format(self.index, self.orbit.__str__())

    def __iter__(self):
        return self
        
    def length(self):
        return self.high

    def curr_elem(self):
        """Gets the current element of the Orbit.

        Returns
        -------
        object
        """

        return self.orbit[self.index]

    def get_index(self, index):
        """Gets the element of the specified index.

        Parameters
        ----------
        index : int

        Returns
        -------
        object
        """

        total = self.index + index
        actual_index = total if total < self.high else total - self.high
        return self.orbit[actual_index]

    def __next__(self):
        self.current += 1

        if self.current < self.high:
            return self.get_index(self.current)

        raise StopIteration

    def _shift_clockwise(self):
        """Shifts the index clockwise by 1 unit.
        
        Returns
        -------
        None
        """

        self.index += 1
        if self.index == len(self.orbit):
            self.index = 0

    def shift(self, n):
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
    
    def get_curr_orbit(self):
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

    def map(self, func):
        """Applies func to all elements in the orbit.
        This is a mutable operation.

        Parameters
        ----------
        func : function
            The function to be applied on the elements. The function should be a unary operator.

        """

        new_orbit = []

        for i in range(self.high):
            transformed = func(self.orbit[i])
            new_orbit.append(transformed)

        self.orbit = new_orbit
