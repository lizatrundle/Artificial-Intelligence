import random
import math

INFINITE = 1000

class LocalSearchPlayground():
    def __init__(self, height, width, houses, max_services):
        self._max_services = max_services
        self._height = height
        self._width = width

        self._houses = set()

        for house in houses:
            self._houses.add((house[0], house[1]))

        self._services = set()

    def __is_a_house(self, row, col):
        return (row, col) in self._houses

    def __is_a_service(self, row, col):
        return (row, col) in self._services

    def __available_positions(self):
        # return all the available cells in the grid

        positions = set()

        for row in range(self._height):
            for col in range(self._width):
                positions.add((row, col))

        # remove the positions occupied by houses and services

        for house in self._houses:
            positions.remove(house)

        for service in self._services:
            positions.remove(service)

        return positions

    def __get_cost(self, services):
        # calculate the sum of distances from houses to the nearest public service

        cost = 0

        for house in self._houses:
            cost += min(
                abs(house[0] - service[0]) + abs(house[1] - service[1])
                for service in services
            )

        return cost

    def __find_neighbors(self, row, col):
        # return the available neighbor coordinates

        candidates = [ (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1) ]
        neighbors = []

        # check if coordinates (r, c) of the neighbor candidates are valid and are available

        for r, c in candidates:
            if 0 <= r < self._height and 0 <= c < self._width:
                if not (r, c) in self._houses and not (r, c) in self._services:
                    neighbors.append((r, c))

        return neighbors

    def hill_climbing(self, maximum=25, verbose=True):
        count = 0

        # initialize services coordinates randomly

        self._services = set()

        for i in range(self._max_services):
            self._services.add(random.choice(list(self.__available_positions())))

        while count < maximum:
            if verbose:
                print (count, "Current state", self.__get_cost(self._services))

            count += 1

            best_neighbors = []
            best_neighbor_cost = INFINITE

            # evaluate the neighbors of the current state

            for service in self._services:
                # the operator * works on any iterable object, it unpacks a tuple or a list,  *service unpacks the row and the column of the service (tuple)

                for replacement in self.__find_neighbors(*service):
                    # generate a neighboring set of services

                    neighbor = self._services.copy()
                    neighbor.remove(service)
                    neighbor.add(replacement)

                    # check if the neighbor is the best so far

                    cost = self.__get_cost(neighbor)

                    if cost < best_neighbor_cost:
                        best_neighbor_cost = cost
                        best_neighbors = [neighbor]
                    elif best_neighbor_cost == cost:
                        best_neighbors.append(neighbor)

            # end when the best neighbor is not better than the current state

            if best_neighbor_cost >= self.__get_cost(self._services):
                return self._services
            else:
                # update the current state with the best neighbor

                self._services = random.choice(best_neighbors)

    """

    def hill_climbing_random_restart(self, maximum, verbose=True):
        # hill climbing with random restarts runs hill-climbing multiple times and returns the best solution

        cost = INFINITE

        for i in range(maximum):

            # set current state to the value returned by hill climbing
            # calculate the cost of the current state

            # if verbose print the iteration and the cost of the current state
            
            # if the cost of the current state is less than the best cost so far
            #    cost = current cost
            #    services = current state
            
    # return services

    def simulated_annealing(self, maximum=100, verbose=True):

        # set current state = initial service locations assigned randomly (see hill climbing: lines 77-80)
        
        # evaluate the neighbors of the current state

        for i in range(maximum):
            # if verbose print the iteration and the cost of the current state

            # find the neighbor states (see hill climbing: lines 88-111)

            # pick a random neighbor and compare its value with the current state (see hill climbing: line 120)

            # delta = cost of the current state - cost of the random neighbor

            # if delta > 0, update the current state with the random neighbor
            #    if verbose print the iteration, the value of delta, and the cost of the current state
            #
            # if delta < 0, calculate the probability exp(delta/temperature(i))
            #    if probability >= 0.5 update the current state with the random neighbor
            #    if verbose print the iteration, the value of delta, and the cost of the current state
            
        # return the current state

    """
    
    def print_map(self, services=[]):
        print ("\nMap \n")

        for i in range(self._height):
            for j in range(self._width):
                if self.__is_a_house(i, j):
                    print ("H", end="")
                elif (i, j) in services:
                    print ("*", end="")
                else:
                    print ("_", end="")

            print (" ")

        if len(services) != 0:
            print ("\nCost is ", self.__get_cost(services), " Services coordinates ", services, "\n")


if __name__=="__main__":

    # create a 5x4 playground with 4 houses and 2 services

    playground = LocalSearchPlayground(height=5, width=9, houses=[(0,2), (1,8), (3,0), (4, 3)], max_services=2)

    # run hill climbing starting with a random location for the public services

    print ("Hill climbing \n")

    locations = playground.hill_climbing()

    playground.print_map(locations)

    """
    
    # run hill climbing with random restart

    print ("Hill climbing with random restart \n")

    locations = playground.hill_climbing_random_restart(25)

    playground.print_map(locations)


    # simulated annealing

    print ("Simulated annealing \n")

    locations = playground.simulated_annealing(100)

    playground.print_map(locations)
    
    """