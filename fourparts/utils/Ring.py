class Ring:
    """A class to represent a circular, repeating structure,
    such as the circle of 5ths.

    Attributes
    ----------
    index : int
        The index of the current pointer to the ring.
    ring : tuple of object
        The tuple of objects that are contained in the ring.
    """

    def __init__(self, ring, index=0):
        """Constructor method of Ring.
        
        Parameters
        ----------
        ring: iterable
            The actual ring.
        index : int
            The pointer towards the element in the ring referred to.
        """

        if index >= len(ring):
            raise IndexError("Ensure index is contained within the length of the ring.")

        self.index = index
        self.ring = tuple(ring)

    def __str__(self):
        return "Index: {0}, Ring: {1}".format(self.index, self.ring.__str__())
        
    def curr_elem(self):
        """Method to get the current element of the Ring.

        Returns
        -------
        object
        """

        return self.ring[self.index]

    def _shift_right(self):
        """Shifts the index to the right by 1 unit.
        
        Returns
        -------
        None
        """

        self.index += 1
        if self.index == len(self.ring):
            self.index = 0

    def _shift_left(self):
        """Shifts the index to the left by 1 unit.

        Returns
        -------
        None
        """

        self.index -= 1
        if self.index == -1:
            self.index = len(self.ring) - 1

    def shift_n(self, n):
        """Shifts the index by n steps.
        
        Parameters
        ----------
        n : int
            If n > 0, it is shifted to the right.
            If n < 0, it is shifted to the left.
        
        Returns
        -------
        object
            The element in the Ring shifted into.
        """

        actual_shifts = n % len(self.ring)

        for _ in range(actual_shifts):
            self._shift_right()

        return self.curr_elem()

    def set_to_zero(self):
        """Set the index of the ring to 0.

        Returns
        -------
        object
            The first element of the Ring.
        """

        self.index = 0
        return self.curr_elem()
