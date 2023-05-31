from pomegranate import *

# rain is an unconditional distribution: P(rain)

rain = Node(DiscreteDistribution({
    "no rain": 0.6,
    "light rain": 0.25,
    "heavy rain": 0.15
}), name="rain")

# traffic jam is a conditional distribution: P(traffic jam | rain)

traffic = Node(ConditionalProbabilityTable([
    ["no rain", "traffic jam", 0.5],
    ["no rain", "no traffic jam", 0.5],
    ["light rain", "traffic jam", 0.7],
    ["light rain", "no traffic jam", 0.3],
    ["heavy rain", "traffic jam", 0.9],
    ["heavy rain", "no traffic jam", 0.1]
], [rain.distribution]), name="traffic")

# bus is a conditional distribution: P(bus | rain and traffic jam)

bus = Node(ConditionalProbabilityTable([
    ["no rain", "traffic jam", "bus on time", 0.4],
    ["no rain", "traffic jam", "bus delayed", 0.6],
    ["no rain", "no traffic jam", "bus on time", 0.9],
    ["no rain", "no traffic jam", "bus delayed", 0.1],
    ["light rain", "traffic jam", "bus on time", 0.3],
    ["light rain", "traffic jam", "bus delayed", 0.7],
    ["light rain", "no traffic jam", "bus on time", 0.5],
    ["light rain", "no traffic jam", "bus delayed", 0.5],
    ["heavy rain", "traffic jam", "bus on time", 0.2],
    ["heavy rain", "traffic jam", "bus delayed", 0.8],
    ["heavy rain", "no traffic jam", "bus on time", 0.5],
    ["heavy rain", "no traffic jam", "bus delayed", 0.5],
], [rain.distribution, traffic.distribution]), name="bus")

# class attendance node is a conditional distribution: P(attendance | bus)

attendance = Node(ConditionalProbabilityTable([
    ["bus on time", "attend on time", 0.9],
    ["bus on time", "attend delayed", 0.1],
    ["bus delayed", "attend on time", 0.7],
    ["bus delayed", "attend delayed", 0.3]
], [bus.distribution]), name="attendance")

# the Bayesian network has 4 random variables: rain, traffic, bus, attendance

model = BayesianNetwork()
model.add_states(rain, traffic, bus, attendance)

# the network edges represent the conditional probability distributions

model.add_edge(rain, traffic)
model.add_edge(rain, bus)
model.add_edge(traffic, bus)
model.add_edge(bus, attendance)

# the model

model.bake()
