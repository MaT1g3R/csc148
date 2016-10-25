"""CSC148 Exercise 1: Basic Object-Oriented Programming

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains starter code for Exercise 1.
It contains two classes that work together:
- SuperDuperManager, which manages all the cars in the system
- Car, a class which represents a single car in the system

Your task is to design and implement the Car class, and then modify the
SuperDuperManager methods so that they make proper use of the Car class.

You may not modify the public interface of any of the SuperDuperManager methods.
We have marked the parts of the code you should change with TODOs, which you
should remove once you've completed them.

Notes:
  1. We'll talk more about private attributes on Friday's class.
     For now, treat them the same as any other instance attribute.
  2. You'll notice we use a trailing underscore for the parameter name
     "id_" in a few places. It is used to avoid conflicts with Python
     keywords. Here we want to have a parameter named "id", but that is
     already the name of a built-in function. So we call it "id_" instead.
"""


class SuperDuperManager:
    """A class responsible for keeping track of all cars in the system.

    === Private Attributes ===
    @type _cars: dict[str, Car]
        A map of unique string identifiers to the corresponding Car.
        For example, _cars['a01'] would be a Car object corresponding to
        the id 'a01'.
    """
    def __init__(self):
        """Initialize a new SuperDuperManager.

        There are no cars in the system when first created.

        @type self: SuperDuperManager
        @rtype: None
        """
        self._cars = {}

    def add_car(self, id_, fuel):
        """Add a new car to the system.

        The new car is identified by the string <id_>, and has initial amount
        of fuel <fuel>.

        Do nothing if there is already a car with the given id.

        @type self: SuperDuperManager
        @type id_: str
        @type fuel: int
        @rtype: None
        """
        # Check to make sure the identifier isn't already used.
        if id_ not in self._cars:
            # TODO: Add the new car.
            self._cars[id_] = Car(id_, fuel)


    def move_car(self, id_, new_x, new_y):
        """Move the car with the given id.

        The car called <id_> should be moved to position (<new_x>, <new_y>).
        Do nothing if there is no car with the given id,
        or if the corresponding car does not have enough fuel.

        @type self: SuperDuperManager
        @type id_: str
        @type new_x: int
        @type new_y: int
        @rtype: None
        """
        if id_ in self._cars:
            # TODO: Move the car with id <id_>.
            # get car with the id <id_>
            this_car = self._cars[id_]

            # get the car's x and y location
            current_x = this_car.x
            current_y = this_car.y

            # calculate fuel usage based on how many blocks moved
            x_diff = abs(current_x - new_x)
            y_diff = abs(current_y - new_y)
            fuel_used = x_diff + y_diff

            # move the car if the car has enough fuel
            if fuel_used <= this_car.fuel:
                this_car.x = new_x
                this_car.y = new_y
                this_car.fuel -= fuel_used


    def get_car_position(self, id_):
        """Return the position of the car with the given id.

        Return a tuple of the (x, y) position of the car with id <id_>.
        Return None if there is no car with the given id.

        @type self: SuperDuperManager
        @type id_: str
        @rtype: (int, int) | None
        """
        if id_ in self._cars:
            # TODO: Get the position of the car with id <id_>.
            # Variable for car with id of <id_>
            this_car = self._cars[id_]
            return this_car.x, this_car.y


    def get_car_fuel(self, id_):
        """Return the amount of fuel of the car with the given id.

        Return None if there is no car with the given id.

        @type self: SuperDuperManager
        @type id_: str
        @rtype: int | None
        """
        if id_ in self._cars:
            # TODO: Get the amount of fuel of the car with id <id_>.
            # Variable for car with id of <id_>
            this_car = self._cars[id_]
            return this_car.fuel

    def dispatch(self, x, y):
        """Move a car to the given location.

        Choose a car to move based on the following criteria:
        (1) Only consider cars that *can* move to the location.
            (Ignore ones that don't have enough fuel.)
        (2) After (1), choose the car that would move the *least* distance to
            get to the location.
        (3) If there is a tie in (2), pick the car whose id comes first
            alphabetically. Use < to compare the strings.
        (4) If no cars can move to the given location, do nothing.

        @type self: SuperDuperManager
        @type x: int
        @type y: int
        @rtype: None
        """


        # TODO: Implement this method!
        # Get all cars
        tmp = dict(self._cars)

        # Get moveable cars' id_
        moveable_id = []
        for car in tmp:
            if (abs(x - tmp[car].x) + abs(y - tmp[car].y)) \
                    <= tmp[car].fuel:
                moveable_id.append(car)

        # a dict for all moveable car objects
        moveable_cars = {}

        # add moveable cars in to the moveable cars dict
        for id_ in moveable_id:
            moveable_cars[id_] = tmp[id_]

        # Choose the least distance car
        # two lists to hold moving distance and keys
        moving_distance = []
        moving_key = []
        for car in moveable_cars:
            moving_distance.append(abs(x - moveable_cars[car].x) +
                                   abs(y - moveable_cars[car].y))

            moving_key.append(moveable_cars[car].id_)

        min_vlue = min(moving_distance)
        min_distance_cars = []

        print(moving_distance)
        print(moving_key)
        # A list to hold one or more min distances
        for distance in moving_distance:
            if distance == min_vlue:
                min_distance_cars.append\
                    (moving_key[moving_distance.index(distance)])


        # Sort id alphabetically
        dispatch_car = sorted(min_distance_cars)[0]
        print(sorted(min_distance_cars))
        print(dispatch_car)

        # Move the car
        self.move_car(dispatch_car, x, y)


# TODO: Design and implement this class.
# TODO: Remember to document all attributes and methods!
class Car:
    """A car in the Super system.

    === Attribute ===
    @type id_: str
    @type fuel: int
    @type x: int
    @type y: int

    """
    def __init__(self, name, f):
        """ Initialize a car
        @type name: str
        @type f: int
        @rtype: none
        """
        self.id_ = name
        self.fuel = f
        self.x = 0
        self.y = 0




if __name__ == '__main__':
    # Run python_ta to ensure this module passes all checks for
    # code inconsistencies and forbidden Python features.
    # Useful for debugging!
    import python_ta
    python_ta.check_errors()

    # testing


    # testing ends

    # Uncomment and run before final submission. This checks for style errors
    # in addition to code inconsistencies and forbidden Python features.
    python_ta.check_all()
