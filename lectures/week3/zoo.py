class Animal:
    """ An animal in the zoo.

    === Attributes ===
    @type name: str
        The name of the animal.

    This is an abstract class, and not ment to be instantiated directly.

    """

    def feed(self):
        """ Feed this animal and have it print out a happy message.
        @type self: Animal
        @rtype: None

        """

        raise NotImplementedError

    def move(self,x,y):
        """ Move this animal and print a moving message

        """

        print("I'm moviing to" + str(x) + ',' + str(y))

    def return_home(self):
        # this will call the move method in the subclass instead of the one in the super class
        self.move(0,0)


# THIS IS INHERITANCE POGCHAMP
# Parenthese indicate inheritance
# Lion is a 'subclass' of animal/ Animal is a 'superclass' of Lion
class Lion(Animal):
    """ A lion in the zoo.
    [NOT NEEDED]
    === Attributes ===
    @type name: str
    ...

    """

    def __init__(self, n):
        self.name = n

    def __str__(self):
        """
        retuns a string representatioon of this object
        @type self: Lion
        @rtype: str
        """
        return "Hi im a lion named {}".format(self.name)


    def feed(self):
        """ feed the lion

        """
        print('yummy')

    def move(self,x,y):
        """ Move this animal and print a moving message

        """
        Animal.move(self,x,y)
        print("IM A FUCKING LION GRRRRRRRRRRR " + str(x) + ',' + str(y))



class Rabbit(Animal):
    """ A Rabbit in the zoo.

    """

    def __init__(self,n):
        self.name = n


    def feed(self):
        """feed the rabbit

        """
        print('oishii, pyon')

if __name__ == '__main__':
    animals = [Lion(),Rabbit(),Rabbit(),Lion(),Lion()]
    for animal in animals:
        animal.feed()
        animal.move(10,20)
