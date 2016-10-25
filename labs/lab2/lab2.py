"""
== Race Registry ==

Context: a system for organizing a 5K running race.

When runners register, they provide their name, email address
and their speed category.  A speed category indicates how quickly they
estimate that they can finish the race.  This allows organizers to start
the runners in groups of roughly equivalent running speed so that
faster runners aren't stuck behind slower runners.  The possible speed
categories are: under 20 minutes, under 30 minutes, under 40 minutes,
and 40 minutes or over.  We need to be able get a list of runners in
a given speed category.  We also need to be able to look up a runner
to find his or her speed category.  Finally, a runner should be able to
change his or her email address and speed category, or withdraw from the
race entirely.
"""

class Runner:
    """ A calss to for the runners
    """
    def __init__(self,name,speed,email):
        """
        @type self: Runner
        @type name: str
        @type email: str
        @type speed: str
        @rtype: none
        """
        self.name = name
        self.email = email
        self.speed = speed



class Runner_manager:
    """


    """

    def __init__(self):
        """
        @type self: Runner_manager
        @rtype: none
        """

        self.runners = {}


    def add_to(self,name,speed,email):

        """
        @type self: dict
        @type runner: Runner
        @rtype: none
        """

        if name not in self.runners:
            self.runners[name] = Runner(name,speed,email)

    def get_runner_by_speed(self,speed_in):
        """
        @type self: Runner_manager
        @type speed: str
        @rtype: list
        """

        runner_list = []

        for guy in self.runners:
            if self.runners[guy].speed == speed_in:
                runner_list.append(self.runners[guy].name)

        return runner_list

    def get_speed_by_name(self,name):
        """
        @type self: Runner_manager
        @type name: str
        @rtype: str
        """
        output = []

        if name in self.runners:
            output.append(self.runners[name].speed)
            return output

    def edit_speed(self,name,speed_edit):

        """

        """

        if name in self.runners:
            self.runners[name].speed = speed_edit

    def edit_email(self,name,email_edit):
        """

        """

        if name in self.runners:
            self.runners[name].email = email_edit

    def kill(self,name):
        """

        """

        if name in self.runners:
            del self.runners[name]








if __name__ == "__main__":

    pass
