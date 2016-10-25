"""Assignment 1 - Distance map (Task 1)

This module contains the class DistanceMap, which is used to store and lookup
distances between cities.  This class does not read distances from the map file.
All reading from files is done in module experiment.

Your task is to design and implement this class.

Do not import any modules here.
"""


class DistanceMap:
    """ A class to store amd look up distance betweeen cities
    === Attributes ===
    @type distances: dict[str, int]
    """
    def __init__(self):
        """ initilize an empty DistanceMap object
        @type self: DistanceMap
        @rtype: none
        """
        self.distances = {}

    def add_distances_pairs(self, c1, c2, dist):
        """ Add one distance pair between two cities
         @type self: DistanceMap
         @type c1: str
         @type c2: str
         @type dist: int
         @rtype: None
        """
        c1 = str.upper(c1)
        c2 = str.upper(c2)
        self.distances[c1 + ', ' + c2] = dist

    def get_distance(self, c1, c2):
        """look up the distance between two cities
        @type self: DistanceMap
        @type c1: str
        @type c2: str
        @rtype: int
        """
        c1 = str.upper(c1)
        c2 = str.upper(c2)
        if c1 + ', ' + c2 in self.distances:
            return self.distances[c1 + ', ' + c2]
        else:
            raise ValueError('This route does not exist')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config='.pylintrc')
