from constraint import *

# professors teaching classes example

csp = Problem()

# variables of the problem: calculus, chemistry, art, history, spanish 

days = ["monday  ", "tuesday", "wednesday"]

# define the variables of the problem and their domains

csp.addVariable("Calculus", days)
csp.addVariable("Chemistry", days)
csp.addVariable("Art", days)
csp.addVariable("History", days)
csp.addVariable("Spanish", days)


# the function day_constraints sets the constraints for the variables

def day_constraints(Calculus, Chemistry, Art, History, Spanish):
    if Calculus != Spanish and Calculus != Art and Calculus != History and Chemistry != Spanish and Chemistry != Art and History != Art and Art != Spanish:
        return True

# define the constraints and the set of variables

csp.addConstraint(day_constraints, ["Calculus","Chemistry","Art","History","Spanish"])

# solve the problem

s = csp.getSolutions()

# print the solutions

for k, day in enumerate(s):
    print("Calculus:{} Chemistry:{} Art:{} History:{} Spanish:{}".format(day["Calculus"],day["Chemistry"], day["Art"], day["History"], day["Spanish"]))
