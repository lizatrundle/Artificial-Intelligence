from search.graph import *
from search.searchPath import * 

 # this is how you can call a function 

    # g(n) ==> actual cost from the initial state to node n 
    # h(n) ==> estimated cost from node n to a goal 
    # f(n) = g(n) + h(n) --> if g(n) == 0 then f(n)= h(n) and it becomes greedy best first search
    # thats why we can use these interchangeably
    #if h(n) == 0 then  f(n) == g(n) ==> we have uniform cost search
    # if f(n) = g(n) + h(n) then we have A*


def print_solution(text, search_output):
    if search_output.explored_nodes == INFINITE or search_output.explored_nodes == None :  # changed this to catch it if its == None
        print (text, "did not find a solution!")
    else:
        s = ""

        while not search_output.path.empty():
            node = search_output.path.remove()

            s = s + node.vertex + "-"

        print (text + " " + s[:-1] + " with total cost " + str(search_output.cost) + " after exploring " + str(search_output.explored_nodes) + " nodes")

if __name__ == '__main__':

    # main method testing for homework 
    distance_to_slu = Graph()
    # i set the heuristic as the cost to reach the goal state from the selected node, by subtracting 1-2 from the routes 
    # to make it an underestimate 
    distance_to_slu.set_vertex('HOME', [['HOLIDAYGYM',20], ['MIAMIAD',13], ['CESIF',18]], [30])
    distance_to_slu.set_vertex('HOLIDAYGYM', [['EMP',10], ['RAMEN',7], ['CESIF',2]], [23])
    distance_to_slu.set_vertex('CESIF', [['RAMEN',6], ['MGR',10], ['MIAMIAD', 5]], [20])
    distance_to_slu.set_vertex('MIAMIAD', [['RAMEN',6], ['MGR',16]], [20])
    distance_to_slu.set_vertex('EMP', [['RAMEN',6],['SLU',18], ['ISLAS',9]], [16])
    distance_to_slu.set_vertex('RAMEN', [['ISLAS',5], ['MGR',7]], [15])
    distance_to_slu.set_vertex('MGR', [['ISLAS',8], ['TINTO',13]], [19])
    distance_to_slu.set_vertex('ISLAS', [['SLU',12],['TINTO',8]], [10])
    distance_to_slu.set_vertex('TINTO', [['SLU',4]],[3])
    distance_to_slu.set_vertex('SLU', [0])

    # print(distance_to_slu._graph)
    # print(distance_to_slu._heuristic)

    print("Informed search:")
    print("--------------------------------")
    print_solution("A* search with astar search --> f(n) = g(n) + h(n), " , distance_to_slu.astar("HOME", "SLU", astar_search))
    print("--------------------------------")
    print_solution("A* search with unfiform cost search --> f(n) = g(n), " , distance_to_slu.astar("HOME", "SLU", uniform_cost_search))
    print("--------------------------------")
    print_solution("A* search with greedy best first search  --> f(n) = h(n), " , distance_to_slu.astar("HOME", "SLU", greedy_search))
    print("--------------------------------")

    grid_graph = Graph()
    grid_graph.set_vertex('A', [['B',1], ['KM',1]], [22])
    grid_graph.set_vertex('B', [['C',2]], [21])
    grid_graph.set_vertex('C', [['D', 3]],[20])
    grid_graph.set_vertex('D', [['E', 4]],[19])
    grid_graph.set_vertex('E', [['F', 5]],[18])
    grid_graph.set_vertex('F', [['G', 6],['XX', 6]],[17])
    grid_graph.set_vertex('G', [['H', 7]],[16])
    grid_graph.set_vertex('H', [['I', 8], ['AA', 8]],[15])
    grid_graph.set_vertex('I', [['J', 9]],[16])
    grid_graph.set_vertex('J', [['K', 10]],[17])
    grid_graph.set_vertex('K', [['L', 11]],[16])
    grid_graph.set_vertex('L', [['M', 12]],[15])
    grid_graph.set_vertex('M', [['N', 13]],[14])
    grid_graph.set_vertex('N', [['O', 14]],[13])
    grid_graph.set_vertex('O', [['P', 15]],[12])
    grid_graph.set_vertex('P', [['Q', 16]],[11])
    grid_graph.set_vertex('Q', [['R', 17]],[10])
    grid_graph.set_vertex('R', [['S', 18]],[9])
    grid_graph.set_vertex('S', [['T', 19]],[8])
    grid_graph.set_vertex('T', [['U', 20]],[7])
    grid_graph.set_vertex('U', [['V', 21]],[6])
    grid_graph.set_vertex('V', [['W', 22]],[5])
    grid_graph.set_vertex('W', [['X', 23]],[4])
    grid_graph.set_vertex('X', [['Y', 24]],[3])
    grid_graph.set_vertex('Y', [['Z', 25]],[2])
    grid_graph.set_vertex('Z', [['ZZ', 22]],[1])
    grid_graph.set_vertex('ZZ', [],)
    grid_graph.set_vertex('KM', [['MM', 2]],[21])
    grid_graph.set_vertex('MM', [['OK', 3]],[20])
    grid_graph.set_vertex('OK', [['ZK', 4]],[19])
    grid_graph.set_vertex('ZK', [['YY', 5]],[18])
    grid_graph.set_vertex('XX', [['YY', 5]],[18])
    grid_graph.set_vertex('YY', [['LT', 6], ["XX",6]], [17])
    grid_graph.set_vertex('LT', [['GG', 7], ["NG", 7]],[16])
    grid_graph.set_vertex('GG', [['KO', 8]],[15])
    grid_graph.set_vertex('KO', [['CO', 9]],[14])
    grid_graph.set_vertex('CO', [['VA', 10], ["CA", 10]],[13])
    grid_graph.set_vertex('VA', [['PA', 11]],[12])
    grid_graph.set_vertex('CA', [['DW', 11]],[14])
    grid_graph.set_vertex('DW', [['WA', 12]],[15])
    grid_graph.set_vertex('WA', [['WX', 13]],[14])
    grid_graph.set_vertex('WX', [['WY', 14]],[13])
    grid_graph.set_vertex('WY', [['WZ', 15]],[12])
    grid_graph.set_vertex('WZ', [['YK', 16]],[11])
    grid_graph.set_vertex('YK', [['YI', 15]],[10])
    grid_graph.set_vertex('YI', [['HH', 14]],[9])
    grid_graph.set_vertex('HH', [['OY', 13]],[8])
    grid_graph.set_vertex('OY', [['SS', 14], ["YO", 12]],[9])
    grid_graph.set_vertex('SS', [['TS', 15]],[8])
    grid_graph.set_vertex('TS', [['KA', 16]],[7])
    grid_graph.set_vertex('KA', [],[6])
    grid_graph.set_vertex('YO', [['PA', 11]],[10])
    grid_graph.set_vertex('PA', [['PC', 12]],[11])
    grid_graph.set_vertex('PC', [['CQ', 13]],[10])
    grid_graph.set_vertex('CQ', [],[9])
    grid_graph.set_vertex('NG', [['QQ', 8]],[15])
    grid_graph.set_vertex('QQ', [['JK', 9]],[14])
    grid_graph.set_vertex('JK', [['IK', 10]],[13])
    grid_graph.set_vertex('IK', [['PP', 11]],[12])
    grid_graph.set_vertex('PP', [['OO', 10], ["AB", 12]],[11])
    grid_graph.set_vertex('OO', [],[10])
    grid_graph.set_vertex('AB', [['BQ', 13]],[10])
    grid_graph.set_vertex('BQ', [],[9])
    grid_graph.set_vertex('AA', [['BB', 9]],[14])
    grid_graph.set_vertex('BB', [['BC', 10]],[13])
    grid_graph.set_vertex('BC', [['BD', 11]],[12])
    grid_graph.set_vertex('BD', [['CC', 12]],[11])
    grid_graph.set_vertex('CC', [['CD', 13]],[10])
    grid_graph.set_vertex('CD', [['DE', 14]],[9])
    grid_graph.set_vertex('DE', [['EF', 15]],[8])
    grid_graph.set_vertex('EF', [['FG', 16]],[7])
    grid_graph.set_vertex('FG', [['GI', 17]],[6])
    grid_graph.set_vertex('GI', [['KK', 18]],[5])
    grid_graph.set_vertex('KK', [['LL', 19]],[4])
    grid_graph.set_vertex('LL', [['MN', 20]],[3])
    grid_graph.set_vertex('MN', [['NN', 21]],[2])
    grid_graph.set_vertex('NN', [['ZZ', 22]],[1])
   
    

    print("Informed search:")
    print("--------------------------------")
    print_solution("A* search with astar search --> f(n) = g(n) + h(n), " , grid_graph.astar("A", "ZZ", astar_search))
    print("--------------------------------")
    print_solution("A* search with unfiform cost search --> f(n) = g(n), " , grid_graph.astar("A", "ZZ", uniform_cost_search))
    print("--------------------------------")
    print_solution("A* search with greedy best first search  --> f(n) = h(n), " , grid_graph.astar("A", "ZZ", greedy_search))
    print("--------------------------------")












    