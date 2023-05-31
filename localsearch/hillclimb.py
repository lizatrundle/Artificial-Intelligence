import random

#
# Local search Hill climbing algorithm
#

class CityMap():
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

        # returns all the available cells in the grid

        positions = set()

        for row in range(self._height):
            for col in range(self._width):
                positions.add((row, col))

        # removes the positions of houses and services

        for house in self._houses:
            positions.remove(house)

        for service in self._services:
            positions.remove(service)

        return positions

    def __get_cost(self, services):

        # calculates the sum of distances from houses to nearest public service

        cost = 0

        for house in self._houses:
            cost += min(
                abs(house[0] - service[0]) + abs(house[1] - service[1])
                for service in services
            )

        return cost

    def __find_neighbors(self, row, col):

        # returns neighbors not containing a house or a public service

        candidates = [ (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1) ]
        neighbors = []

        # checks if coordinates (r, c) of the neighbor candidates are valid and are not locations of a house or a service

        for r, c in candidates:
            if 0 <= r < self._height and 0 <= c < self._width:
                if not (r, c) in self._houses and not (r, c) in self._services:
                    neighbors.append((r, c))

        return neighbors

    def hill_climbing(self, maximum=100, verbose=False):      
        count = 0

        # initializes the locations of the services randomly

        self._services = set()

        for i in range(self._max_services):
            self._services.add(random.choice(list(self.__available_positions())))

        # runs the maximum number of iterations

        while count < maximum:
            count += 1
            best_neighbors = []
            best_neighbor_cost = None

            # analyzes the services to reallocate

            for service in self._services:
                # analyzes the neighbors of a public service (pharmacy, school, police station, ...)

                for replacement in self.__find_neighbors(*service):
                    # generates a neighboring set of services

                    neighbor = self._services.copy()
                    neighbor.remove(service)
                    neighbor.add(replacement)

                    # check if the neighbor is the best so far

                    cost = self.__get_cost(neighbor)

                    if best_neighbor_cost is None or cost < best_neighbor_cost:
                        best_neighbor_cost = cost
                        best_neighbors = [neighbor]
                    elif best_neighbor_cost == cost:
                        best_neighbors.append(neighbor)

            # end when the best neighbor is not better than the current state

            if best_neighbor_cost >= self.__get_cost(self._services):
                return self._services
            else:
                # updates the current state to a highest-valued neighbor

                if verbose:
                    print ("Better neighbor found with cost ", best_neighbor_cost)

                self._services = random.choice(best_neighbors)

    # def hill_climbing_random_restart(self, maximum, verbose=False):
    #     # runs hill-climbing multiple times and returns the best solution
    # return best_services

    # homework

    def print_map(self, services=[]):
        print ("\nCity Map \n")

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
            print ("\nCost is ", self.__get_cost(services), " Services locations ", services, "\n")


if __name__=="__main__":

    # creates a new city map with houses and services

    city = CityMap(height=5, width=9, houses=[(0,2), (1,8), (3,0), (4, 3)], max_services=2)

    # runs hill climbing starting with a random location for the public services

    print ("\nHill climbing")

    locations = city.hill_climbing(verbose=True)

    city.print_map(locations)
