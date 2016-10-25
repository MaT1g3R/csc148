"""Assignment 1 - Scheduling algorithms (Task 4)

This module contains the abstract Scheduler interface, as well as the two
classes RandomScheduler and GreedyScheduler, which implement the two
scheduling algorithms described in the handout.

Your task is to implement RandomScheduler and GreedyScheduler.
You may *not* change the public interface of these classes, except that
you must write appropriate constructors for them.  The two constructors do not
need to have the same signatures.

Any attributes you use must be private, so that the public interface is exactly
what is specified by the Scheduler abstract class.
"""

from random import shuffle
from container import PriorityQueue


class Scheduler:
    """A scheduler, capable of deciding what parcels go onto which trucks, and
    what route each truck will take.

    This is an abstract class.  Only child classes should be instantiated.

    You may add *private* methods to this class so make them available to both
    subclasses.
    """
    def schedule(self, parcels, trucks, verbose):
        """Schedule the given parcels onto the given trucks.

        Mutate the trucks so that they store information about which
        parcels they will deliver and what route they will take.
        Do *not* mutate the parcels.

        Return the parcels that do not get scheduled onto any truck, due to
        lack of capacity.

        If <verbose> is True, print step-by-step details regarding
        the scheduling algorithm as it runs.  This is *only* for debugging
        purposes for your benefit, so the content and format of this
        information is your choice; we will not test your code with <verbose>
        set to True.

        @type self: Scheduler
        @type parcels: list[Parcel]
            The parcels to be scheduled for delivery.
        @type trucks: list[Truck]
            The trucks that can carry parcels for delivery.
        @type verbose: bool
            Whether or not to run in verbose mode.
        @rtype: list[Parcel]
            The parcels that did not get scheduled onto any truck, due to
            lack of capacity.
        """
        raise NotImplementedError


class RandomScheduler(Scheduler):
    """ A random scheduler, this calss is dumb and sort stuff randomly
    """

    def schedule(self, parcels, trucks, verbose):
        """ schedule deliveries randomly

        The random algorithm will go through the parcels in random order.
        For each parcel, it will schedule it onto a randomly chosen truck
        (from among those trucks that have capacity to add that parcel).
        Because of this randomness,
        each time you run your random algorithm on a given problem,
        it may generate a different solution.

        @type self: RandomScheduler
        @type parcels: list[Parcels]
        @type trucks: list[Truck]
        @type verbose: bool
        @rtype: list[Parcel]
            The parcels that did not get scheduled
             onto any truck, due to
            lack of capacity.
        """
        shuffle(trucks)
        shuffle(parcels)
        left_overs = parcels[:]

        for parcel in parcels:
            for truck in trucks:
                if truck.check_volume(parcel):
                    truck.load(parcel)
                    left_overs.remove(parcel)
                    break
        return left_overs


class GreedyScheduler(Scheduler):
    """ Greedily schedules parcels onto trucks.
    there are 4 parcel arrangements and 2 trucls arrangements
    therefore a total of 8 configs of this class.

    Trucks config(Assuming the trucks can fit the parcel):
        from least avaliable volume to most avaliable volume
        from most avaliable volume to least avaliable volume

    And for each truck config we have 2 parcel configs,
    and 2 ordering methods for the configs:

        for the parcel volume config, we have:
            from smallest volume to the largest volume
            from largest volume to the smallest volume

        for the parcel desinition config, we have:
            from alphabetically front most desinition name to
            alphabetically back most desinition name
                i.e: from A to Z
            from alphabetically back most desinition name to
             alphabetically front most desinition name
                i.e: from Z to A

    === Attributes ===
    @type parcel_priority: str
    @type parcel_order: str
    @type truck_order: str
    @type parcels: list[Parcels]
    @type trucks: list[Truck]
    @type verbose: bool

    === representation invariant ===
    parcel_priority in ['non-decreasing', 'non-increasing']
    parcel_order in ['volume', 'destination']
    truck_order in ['non-decreasing', 'non-increasing']
    in other words, don't try to initilize the class
    if the parameter you use isn't excatly stated as above
    """

    def __init__(self, parcel_priority, parcel_order, truck_order):
        """ Initilize the greed
        @type parcel_priority: str
        @type parcel_order: str
        @type truck_order: str
        @rtype: None
        """
        if parcel_priority in ['volume', 'destination'] and \
                parcel_order in \
                ['non-decreasing', 'non-increasing'] and \
                truck_order in ['non-decreasing', 'non-increasing']:
            self.parcel_priority = parcel_priority
            self.parcel_order = parcel_order
            self.truck_order = truck_order
            self.parcels = []
            self.trucks = []
            self.verbose = []
        else:
            raise ValueError('Illegal Argument')

    def arrange_trucks(self):
        """ arrange trucks for either
        one of the two truck configs
         @type self: GreedyScheduler
         @rtype: None
        """
        if self.truck_order == 'non-decreasing':
            truck_pirority_queue = PriorityQueue(truck_less)
            for truck in self.trucks:
                truck_pirority_queue.add(truck)
            self.trucks = []
            while not truck_pirority_queue.is_empty():
                self.trucks.append(truck_pirority_queue.remove())

        elif self.truck_order == 'non-increasing':
            truck_pirority_queue = PriorityQueue(truck_more)
            for truck in self.trucks:
                truck_pirority_queue.add(truck)
            self.trucks = []
            while not truck_pirority_queue.is_empty():
                self.trucks.append(truck_pirority_queue.remove())

    def arrange_parcels(self):
        """ Arrange parcels according to the greedy setup
         @type self: GreedyScheduler
         @rtype: None
        """
        if self.parcel_priority == 'volume':
            if self.parcel_order == 'non-increasing':
                parcel_pirority_queue = PriorityQueue(parcel_small)
                for parcel in self.parcels:
                    parcel_pirority_queue.add(parcel)
                self.parcels = []
                while not parcel_pirority_queue.is_empty():
                    self.parcels = [parcel_pirority_queue.remove()] \
                                   + self.parcels

            elif self.parcel_order == 'non-decreasing':
                parcel_pirority_queue = PriorityQueue(parcel_large)
                for parcel in self.parcels:
                    parcel_pirority_queue.add(parcel)
                self.parcels = []
                while not parcel_pirority_queue.is_empty():
                    self.parcels = [parcel_pirority_queue.remove()] \
                                   + self.parcels

        elif self.parcel_priority == 'destination':
            if self.parcel_order == 'non-decreasing':
                parcel_pirority_queue = PriorityQueue(parcel_front)
                for parcel in self.parcels:
                    parcel_pirority_queue.add(parcel)
                self.parcels = []
                while not parcel_pirority_queue.is_empty():
                    self.parcels = [parcel_pirority_queue.remove()] \
                                   + self.parcels

            elif self.parcel_order == 'non-increasing':
                parcel_pirority_queue = PriorityQueue(parcel_back)
                for parcel in self.parcels:
                    parcel_pirority_queue.add(parcel)
                self.parcels = []
                while not parcel_pirority_queue.is_empty():
                    self.parcels = [parcel_pirority_queue.remove()] \
                                   + self.parcels

    def schedule(self, parcels, trucks, verbose):
        """ Schedlue using the greed
        @type self: GreedyScheduler
        @type parcels: list[Parcels]
        @type trucks: list[Truck]
        @type verbose: bool
        @rtype: list[Parcel]
            returns a list of unscheduled parcels
        """
        self.parcels = parcels
        self.trucks = trucks
        leftover_parcels = self.parcels[:]

        self.arrange_parcels()
        self.arrange_trucks()

        for _p in self.parcels:
            found_same_dest = False
            for _t in self.trucks:
                if _t.check_volume(_p) and _p.destination in _t.desinations:
                    _t.load(_p)
                    leftover_parcels.remove(_p)
                    found_same_dest = True
                    break
            for _t in self.trucks:
                if _t.check_volume(_p) and not found_same_dest:
                    _t.load(_p)
                    leftover_parcels.remove(_p)
                    break
            self.arrange_trucks()

        self.arrange_trucks()
        return leftover_parcels


def truck_less(a, b):
    """  Gives trucks with less avaliabvle volume priority
    @type a: Truck
    @type b: Truck
    @rtype: bool
    """
    return a.avaliable_volume() < b.avaliable_volume()


def truck_more(a, b):
    """ Gives trucks with more avaliable volume priority
    @type a: Truck
    @type b: Truck
    @rtype: bool
    """
    return a.avaliable_volume() > b.avaliable_volume()


def parcel_small(a, b):
    """ Gives the smaller parcel pirority
     @type a: Parcel
     @type b: Parcel
     @rtype: bool
    """
    return a.volume < b.volume


def parcel_large(a, b):
    """ Gives the larger parcel pirority
     @type a: Parcel
     @type b: Parcel
     @rtype: bool
    """
    return a.volume > b.volume


def parcel_front(a, b):
    """ Gives the parcel with destination that
    comes firt alphabetically pirority
    @type a: Parcel
    @type b: Parcel
    @rtype: bool
    """
    return a.destination < b.destination


def parcel_back(a, b):
    """ Gives the parcel with destination that comes
    last alphabetically pirority
    @type a: Parcel
    @type b: Parcel
    @rtype: bool
    """
    return a.destination > b.destination


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config='.pylintrc')
