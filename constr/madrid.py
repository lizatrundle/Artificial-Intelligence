from constraint import *

# Australia map coloring

csp = Problem()

# variables of the problem: Tetuan, Moncloa, Chamartin, Distrito, Salamanca, Chamberi, Retiro, Arganzuela 

colors = ["red", "green", "blue ", "yellow"]

# define the variables of the problem and their color domains

csp.addVariable("Tetuan", colors)
csp.addVariable("Moncloa", colors)
csp.addVariable("Chamartin", colors)
csp.addVariable("Distrito", colors)
csp.addVariable("Salamanca", colors)
csp.addVariable("Chamberi", colors)
csp.addVariable("Retiro", colors)
csp.addVariable("Arganzuela", colors)

# the function color_constraints sets the constraints for the variables

def color_constraints(Tetuan, Moncloa, Chamartin, Distrito, Salamanca, Chamberi, Retiro, Arganzuela):
    if Tetuan != Moncloa and Tetuan != Chamartin and Tetuan != Chamberi and Moncloa != Chamberi and Moncloa != Distrito and Moncloa != Arganzuela and Chamberi != Chamartin and Chamberi != Salamanca and Chamberi != Distrito and Distrito != Arganzuela and Distrito != Retiro and Distrito != Salamanca and Chamartin != Salamanca and Salamanca != Retiro and Retiro != Arganzuela:
        return True

# define the constraints and the set of variables

csp.addConstraint(color_constraints, ["Tetuan", "Moncloa", "Chamartin", "Distrito", "Salamanca", "Chamberi", "Retiro", "Arganzuela"])

# solve the problem

s = csp.getSolutions()

# print the solutions

for k, color in enumerate(s):
    print("Tetuan: {} Moncloa: {} Chamartin: {} Distrito: {} Salamanca: {} Chamberi: {} Retiro: {} Arganzuela: {}".format(color["Tetuan"], color["Moncloa"], color["Chamartin"], color["Distrito"], color["Salamanca"], color["Chamberi"], color["Retiro"], color["Arganzuela"]))
