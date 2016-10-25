"""Assignment 1 - Domain classes (Task 2)

This module contains all of the classes required to represent the entities
in the experiment, including at least a class Parcel and a class Truck.
"""

class Parcel:

    """ Represent a single parcel object
    === Attributes ===
    @type pid: int
    @type source: str
    @type destination : str
    @type volume
    """

    def __init__(self, pid, source, destination, volume):
        """ initialize a parcel
        @type self: Parcel
        @type source: str
        @type destination : str
        @type volume: int
        """
        self.pid = pid
        self.source = source
        self. destination = destination
        self. volume = volume


class ParcelManager:
    """ A parcel manager class for all of trhe parcels
    === Attributes ===
    @type all_parcels: list[Parcel]
    """

    def __init__(self):
        """ initizlize an empty dict to hold all parcels
        @type self: ParcelManager
        @rtype: None
        """
        self.all_parcels = []

    def add_parcel(self, pid, source, destination, volume):
        """ Add one parcel to the manager
        @type self: ParcelManager
        @type pid: int
        @type source: str
        @type destination: str
        @type volume: int
        @rtype:none
        """
        self.all_parcels.append(Parcel(pid, source, destination, volume))

    def get_all(self):
        """return all items in the manager in a list
         @type self: ParcelManager
         @rtype: list[Parcel]
        """
        return self.all_parcels


class Truck:
    """ A single truck object
    === Attributes ===
    @type tid: int
    @type max_volume: int
    @type current_volume: int
    @type current_parcels: list[Parcel]
    @type desinations: list[str]
    """
    def __init__(self, tid, m_v, depot_location):
        """ initilize the truck with a max volume and 0 current volume
         @type self: Truck
         @type tid: int
         @type m_v: int
         @rtype: None
        """
        self.tid = tid
        self.max_volume = m_v
        self.current_volume = 0
        self.current_parcels = []
        self.desinations = []
        self.deopt_location = depot_location

    def check_volume(self, parcel):
        """ Checks if the truck has enough volume to load the parcel
        @type self: Truck
        @type parcel: Parcel
        @rtype: bool
        """
        return (self.max_volume - self.current_volume - parcel.volume) >= 0

    def avaliable_volume(self):
        """ retuns the avaliable volume on the truck
        @type self: Truck
        @rtype: int
        """
        return self.max_volume - self.current_volume

    def load(self, parcel):
        """ Attempt to load a parcel onto a truck
        @type parcel: Parcel
        @rtype: None
        """
        if self.check_volume(parcel):
            self.current_volume += parcel.volume
            self.current_parcels.append(parcel)
            if parcel.destination not in self.desinations:
                self.desinations.append(parcel.destination)
        else:
            raise ValueError('Not enough space in the truck')


class TruckManager:
    """ A manager for all of the trucks
    === Attributes ===
    @type all_trucks: list[Truck]

    """
    def __init__(self):
        """ initilize the all_tucks dict
        @type self: TruckManager
        @rtype: None
        """
        self.all_trucks = []

    def add_truck(self, tid, capacity, depot_location):
        """ Add a truck to the manager
         @type self: TruckManager
         @type tid: int
         @type capacity: int
         @type depot_location: str
         @rtype: None
        """
        self.all_trucks.append(Truck(tid, capacity, depot_location))

    def get_all(self):
        """return all trucks in the manager in a list
         @type self: TruckManager
         @rtype: list[Truck]
        """
        return self.all_trucks

if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='.pylintrc')
    import doctest
    doctest.testmod()
