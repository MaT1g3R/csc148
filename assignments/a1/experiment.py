"""Assignment 1 - Running experiments (Tasks 5 & 6)

This module contains class SchedulingExperiment.  It can create an experiment
with input data and an algorithm configuration specified in a dictionary, then
run the experiment, generate statistics as the result of the experiment, and
(optionally) report the statistics.

This module is responsible for all the reading of data from the data files.

To test your code, we will construct instances of SchedulingExperiment, call
its methods, and examine the dictionary of statistics that method run
returns.

If you defined any domain classes other than Parcel and Truck, you may import
them here.  You may not import external libraries.
"""
from scheduler import RandomScheduler, GreedyScheduler
from domain import ParcelManager, TruckManager
from distance_map import DistanceMap


class SchedulingExperiment:
    """An experiment in scheduling parcels for delivery.

    To complete an experiment involves four stages:

    1. Read in all data from necessary files, and create corresponding objects.
    2. Run a scheduling algorithm to assign parcels to trucks.
    3. Compute statistics showing how good the assignment of parcels to trucks
       is.
    4. Report the statistics from the experiment.

    === Attributes ===
    @type depot_location: str
    @type parcels: list[Parcel]
    @type trucks: list[Truck]
    @type distance_map: DistanceMap
    @type algorithm: str
    @type orders = dict[str]
    @type verbose: bool
    """
    def __init__(self, config):
        """Initialize a new experiment from a configuration dictionary.

        Precondition: <config> contains keys and values as specified
        in Assignment 1.

        @type config: dict[str, str]
            The configuration for this experiment, including
            the data files and algorithm configuration to use.
        @rtype: None
        """
        self.depot_location = config['depot_location']
        self.parcels = read_parcels(config['parcel_file']).get_all()
        self.trucks = read_trucks(config['truck_file'],
                                  self.depot_location).get_all()
        self.distance_map = read_distance_map(config['map_file'])
        self.algorithm = config['algorithm']
        self.orders = dict()
        self.orders['parcel_priority'] = config['parcel_priority']
        self.orders['parcel_order'] = config['parcel_order']
        self.orders['truck_order'] = config['truck_order']
        self.verbose = config['verbose'] == 'true'

    def run(self, report=True):
        """Run the experiment and return statistics on the outcome.

        If <report> is True, print a report on the statistics from this
        experiment.  Either way, return the statistics in a dictionary.

        If <self.verbose> is True, print step-by-step details
        regarding the scheduling algorithm as it runs.

        @type self: SchedulingExperiment
        @type report: bool
            Whether or not to print a report on the statistics.
        @rtype: dict[str, int | float]
            Statistics from this experiment. Keys and values are as specified
            in Step 6 of Assignment 1.
        """
        if report:
            if self.algorithm == 'random':
                _run = RandomScheduler()
                unscheduled = _run.schedule\
                    (self.parcels, self.trucks, self.verbose)
                stats_dict = self._compute_stats()
                stats_dict['unscheduled'] = len(unscheduled)
                print(stats_dict)
                return stats_dict
            else:
                _run = GreedyScheduler(self.orders['parcel_priority'],
                                       self.orders['parcel_order'],
                                       self.orders['truck_order'])
                unscheduled = _run.schedule(self.parcels,
                                            self.trucks, self.verbose)
                stats_dict = self._compute_stats()
                stats_dict['unscheduled'] = len(unscheduled)
                print(stats_dict)
                return stats_dict
        else:
            if self.algorithm == 'random':
                _run = RandomScheduler()
                unscheduled = _run.schedule(self.parcels,
                                            self.trucks, self.verbose)
                stats_dict = self._compute_stats()
                stats_dict['unscheduled'] = len(unscheduled)
                return stats_dict
            else:
                _run = GreedyScheduler(self.orders['parcel_priority'],
                                       self.orders['parcel_order'],
                                       self.orders['truck_order'])
                unscheduled = _run.schedule(self.parcels,
                                            self.trucks, self.verbose)
                stats_dict = self._compute_stats()
                stats_dict['unscheduled'] = len(unscheduled)
                return stats_dict

    def _compute_stats(self):
        """Compute the statistics for this experiment.

        Precondition: _run has already been called.

        @type self: SchedulingExperiment
        @rtype: Dict[str, int | float]
            Statistics from this experiment. Keys and values are as specified
            in Step 6 of Assignment 1.
        """
        stats_dict = dict()
        stats_dict['fleet'] = len(self.trucks)

        unused_trucks = 0
        used_trucks = self.trucks[:]

        for truck in self.trucks:
            if truck.current_parcels == []:
                unused_trucks += 1
                used_trucks.remove(truck)
        stats_dict['unused_trucks'] = unused_trucks

        total_dist = 0

        for truck in used_trucks:
            current_city = self.depot_location
            for dest in truck.desinations:
                total_dist += self.distance_map.get_distance(current_city, dest)
                current_city = dest

        avg_dist = float(total_dist/len(used_trucks))
        stats_dict['avg_distance'] = avg_dist

        fullness = []
        for truck in used_trucks:
            fullness.append(float(truck.current_volume/truck.max_volume))

        stats_dict['avg_fullness'] = (sum(fullness)/len(fullness))*100

        stats_dict['unused_space'] = 0
        for truck in used_trucks:
            stats_dict['unused_space'] += truck.avaliable_volume()

        return stats_dict

    def _print_report(self):
        """Report on the statistics for this experiment.

        This method is *only* for debugging purposes for your benefit, so
        the content and format of the report is your choice; we
        will not call your run method with <report> set to True.

        Precondition: _compute_stats has already been called.

        @type self: SchedulingExperiment
        @rtype: None
        """

        pass


def read_parcels(parcel_file):
    """Read parcel data from <parcel_file> and return all_parcels

    @type parcel_file: str
        The name of a file containing parcel data in the form specified in
        Assignment 1.
    @rtype: ParcelManager

    """

    all_parcels = ParcelManager()
    with open(parcel_file, 'r') as file:
        for line in file:
            tokens = line.strip().split(',')
            pid = int(tokens[0].strip())
            source = tokens[1].strip()
            destination = tokens[2].strip()
            volume = int(tokens[3].strip())
            all_parcels.add_parcel(pid, source, destination, volume)

    return all_parcels


def read_distance_map(distance_map_file):
    """Read distance data from <distance_map_file> and return all_distances

    @type distance_map_file: str
        The name of a file containing distance data in the form specified in
        Assignment 1.
    @rtype: DistanceMap

    """
    all_distances = DistanceMap()

    with open(distance_map_file, 'r') as file:
        for line in file:
            tokens = line.strip().split(',')
            c1 = tokens[0].strip()
            c2 = tokens[1].strip()
            dist = int(tokens[2].strip())
            all_distances.add_distances_pairs(c1, c2, dist)

    return all_distances


def read_trucks(truck_file, depot_location):
    """Read truck data from <truck_file> and return all_trucks

    @type truck_file: str
        The name of a file containing truck data in the form specified in
        Assignment 1.
    @type depot_location: str
        The city where all the trucks (and packages) are at the start of the
        experiment.
    @rtype: TruckManager

    """
    all_trucks = TruckManager()

    with open(truck_file, 'r') as file:
        for line in file:
            tokens = line.strip().split(',')
            tid = int(tokens[0])
            capacity = int(tokens[1])
            all_trucks.add_truck(tid, capacity, depot_location)

    return all_trucks


def sanity_check(config_file):
    """Configure and run a single experiment on the scheduling problem
    defined in <config_file>

    Precondition: <config_file> is a json file with keys and values
    as in the dictionary format defined in Assignment 1.

    @type config_file: str
    @rtype: None
    """
    import json
    with open(config_file, 'r') as file:
        configuration = json.load(file)
    # Create and run an experiment with that configuration.
    experiment = SchedulingExperiment(configuration)
    experiment.run(report=True)

if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='.pylintrc')

    # ------------------------------------------------------------------------
    # The following code can be used as a quick and dirty check to see if your
    # experiment can run without errors. Feel free to uncomment it for testing
    # purposes, but you should remove it before submitting your final version.
    # ------------------------------------------------------------------------
    sanity_check('data/demo.json')
