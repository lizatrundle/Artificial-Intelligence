import pomegranate



# electronic failure is an unconditional distribution: P(electronic)

electronic = Node(DiscreteDistribution({
    "electronic failure": 0.1,
    "no electronic failure": 0.9
}), name="electronic")

# mechanic failure is an unconditional distribution: P(mechanic)

mechanic = Node(DiscreteDistribution({
    "mechanic failure": 0.2,
    "no mechanic failure": 0.8
}), name="mechanic")

# car failure is a conditional distribution: P(failure | electronic and mechanic)

car_failure = Node(ConditionalProbabilityTable([
    ["electronic failure", "mechanic failure", "car does not work", 1.0],
    ["electronic failure", "mechanic failure", "car works", 0.0],
    ["electronic failure", "no mechanic failure", "car does not work", 1.0],
    ["electronic failure", "no mechanic failure", "car works", 0.0],
    ["no electronic failure", "mechanic failure", "car does not work", 0.5],
    ["no electronic failure", "mechanic failure", "car works", 0.5],
    ["no electronic failure", "no mechanic failure", "car does not work", 0.0],
    ["no electronic failure", "no mechanic failure", "car works", 1.0],
], [electronic.distribution, mechanic.distribution]), name="car_failure")

# the Bayesian network has 3 random variables: electronic, mechanic, car_failure

model = BayesianNetwork()
model.add_states(electronic, mechanic, car_failure)


# the network edges represent the conditional probability distributions

model.add_edge(electronic, car_failure)
model.add_edge(mechanic, car_failure)

# the model

model.bake()
