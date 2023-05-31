import random
import math

INFINITE = 1000
# difference between hill climbing with random restart and simulated annealing 
# random restart --> running multiple times to get the best solution 
# annealing means the more we run hill climbing the less probability of getting an error 
# get a random neighbor, calculate cost 
# find delta --> cost of current state - cost of the random neighbor state 
# delta can be > 0 or < 0, if its == 0 then the current solution and random solution are the same 
# if delta is positive then the current state is worse , if delta is negative then current state is better 

#simulated annealing is the same as hill climbing, but we just add the delta for the annealing 
# at beginning of algortihm, it will be likely to take a worse solution, but at the end it will be more likely to take the better solution

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
    
    def __temperature(self, i):
        return 1/(.01+i*.01) if i < 25 else 1/(.03 + ( i-25)*.05) 

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

    
    def hill_climbing_random_restart(self, maximum, verbose=True):
        # hill climbing with random restarts runs hill-climbing multiple times and returns the best solution

        cost = INFINITE

        for i in range(maximum):
            
            current_state = self.hill_climbing(maximum)
            cur_cost = self.__get_cost(current_state)
            if verbose:
                print (i, "Current state", cur_cost)
                # count+=1
        
            if cur_cost < cost:
                cost = cur_cost
                self._services = current_state
            

        return self._services
    

    def simulated_annealing(self, maximum=100, verbose=True):
        self._services = set()
        
        for i in range(self._max_services):
            self._services.add(random.choice(list(self.__available_positions())))
            # services is the current state 

        for i in range(maximum):
            if verbose:
                print (i, "Current state", self.__get_cost(self._services))

        # set current state = initial service locations assigned randomly (see hill climbing: lines 77-80)
        
        # evaluate the neighbors of the current state

            best_neighbors = []
            best_neighbor_cost = INFINITE

            for service in self._services:
            
                for replacement in self.__find_neighbors(*service):
                  

                    neighbor = self._services.copy()
                    neighbor.remove(service)
                    neighbor.add(replacement)

                    cost = self.__get_cost(neighbor)

                    if cost < best_neighbor_cost:
                        best_neighbor_cost = cost
                        best_neighbors = [neighbor]
                    elif best_neighbor_cost == cost:
                        best_neighbors.append(neighbor)
                    
           
            random_neighbor = random.choice(best_neighbors)
            
            delta =  self.__get_cost(self._services) - self.__get_cost(random_neighbor)
            
            if delta > 0:
                self._services = random_neighbor
                if verbose:
                    print (i, " delta", delta, " cost of current state ", self.__get_cost(self._services))
            elif delta < 0:
                probability = math.exp(delta/self.__temperature(i))
                if probability >= .5:
                    self._services = random_neighbor
                if verbose:
                    print (i, " delta", delta, " cost of current state ", self.__get_cost(self._services))
            
        return self._services
          
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

    # create a 12x12 playground with 11 houses and 11 services

    # coordinates go (down y, over x)
   
    playground = LocalSearchPlayground(height=12, width=12, houses=[(1,2), (5,0), (11,0), (8, 2), (4,3), (11,4), (2,7),(5,6),(0,11),(9,8), (6,11)], max_services=4)

    # run hill climbing starting with a random location for the public services

    print ("Hill climbing \n")

    locations = playground.hill_climbing()

    playground.print_map(locations)

 
    
    # run hill climbing with random restart

    print ("Hill climbing with random restart \n")

    locations = playground.hill_climbing_random_restart(25)

    playground.print_map(locations)


    # simulated annealing

    print ("Simulated annealing \n")

    locations = playground.simulated_annealing(100)

    playground.print_map(locations)
    
 