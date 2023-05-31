from constraint import *

# Australia map coloring

csp = Problem()

# variables of the problem: WA, NT, SA, Q, NSW, V, T and their possible solutions

colors = ["red  ", "green", "blue "]

# define the variables of the problem and their color domains

csp.addVariable("WA", colors)
csp.addVariable("NT", colors)
csp.addVariable("SA", colors)
csp.addVariable("Q", colors)
csp.addVariable("NSW", colors)
csp.addVariable("V", colors)
csp.addVariable("T", colors)

# the function color_constraints sets the constraints for the variables

def color_constraints(WA, NT, SA, Q, NSW, V, T):
    if WA != NT and WA != SA and NT != SA and NT != Q and SA != Q and SA != NSW and SA != V and NSW != V and NSW != Q:
        return True

# define the constraints and the set of variables

csp.addConstraint(color_constraints, ["WA","NT","SA","Q","NSW","V","T"])

# solve the problem

s = csp.getSolutions()

# print the solutions

for k, color in enumerate(s):
    print("WA:{} NT:{} SA:{} Q:{} NSW:{} V:{} T:{}".format(color["WA"], color["NT"], color["SA"], color["Q"], color["NSW"], color["V"], color["T"]))
