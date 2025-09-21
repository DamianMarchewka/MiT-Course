###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    trips = []
    cows_copy = cows.copy()

    while cows_copy:
        current_trip = []
        remaining_limit = limit

        sorted_cows = sorted(cows_copy.items(), key=lambda item: item[1], reverse=True)

        while sorted_cows:
            cow_added = False
            for cow, weight in sorted_cows:
                if weight <= remaining_limit:
                    current_trip.append(cow)
                    remaining_limit -= weight
                    del cows_copy[cow]
                    cow_added = True
                    break
            if not cow_added:
                break
            sorted_cows = sorted(cows_copy.items(), key=lambda item: item[1], reverse=True)

        trips.append(current_trip)

    return trips


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cow_names = list(cows.keys())
    best_partition = None
    best_trips_count = float("inf")

    for partition in get_partitions(cow_names):
        valid = True
        for trip in partition:
            total_weight = sum(cows[cow] for cow in trip)
            if total_weight > limit:
                valid = False
                break
        if valid:
            if len(partition) < best_trips_count:
                best_partition = partition
                best_trips_count = len(partition)
                if best_trips_count == 1:
                    break

    return best_partition

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data.txt")
    limit = 10

    start = time.time()
    greedy_result = greedy_cow_transport(cows, limit)
    greedy_time = time.time() - start

    start = time.time()
    brute_result = brute_force_cow_transport(cows, limit)
    brute_time = time.time() - start

    print("Result of Greedy algorythm:")
    print(" Number of trip: {}".format(len(greedy_result)))
    print(" Execution time: {:.4f} seconds".format(greedy_time))

    print("\nResult Brute algorythm:")
    print(" Number of trip: {}".format(len(brute_result)))
    print(" Execution time: {:.4f} seconds".format(brute_time))


if __name__ == "__name__":
    compare_cow_transport_algorithms()

"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))
print("")
print(compare_cow_transport_algorithms())