import numpy as np

# implementation of two-input logic gates OR, NOR, AND, NAND, and XOR using a perceptron and the step function

def step(v):
    return 1 if v >=0 else 0

def perceptron(inputs, weights, bias):
    return step(np.dot(np.array(weights), np.array(inputs)) + bias)

# NOT gate: g(- x), weights [-1], bias = 0

def not_gate(x):
    weights = -1
    bias = 0

    return perceptron(x, weights, bias)

# OR gate: g(-1 + x1 + x2), weights [1, 1], bias = -1

def or_gate(x):
    weights = [1, 1]
    bias = -1

    return perceptron(x, weights, bias)

# NOR gate: g(- x1 - x2), weights [-1, -1], bias = 0

def nor_gate(x):
    weights = [-1, -1]
    bias = 0

    return perceptron(x, weights, bias)

# NOR gate implemented with OR and NOT

def nor_gate_not(x):
    return not_gate(or_gate(x))

# AND gate: g(-2 + x1 + x2), weights [1, 1], bias = -2

def and_gate(x):
    weights = [1, 1]
    bias = -2

    return perceptron(x, weights, bias)

# NAND gate: g(), weights [], bias =

def nand_gate(x):
    weights = [-1, -1]
    bias = 1

    return perceptron(x, weights, bias)

# NAND gate implemented with AND and NOT

def nand_gate_not(x):
    return not_gate(and_gate(x))


def xor_gate(x):
    return and_gate[(or_gate(x), nand_gate(x))]


if __name__=="__main__":

    # testing the NOT gate

    print ("NOT gate \n")

    for t in range(2):
        print ("NOT ({}) = {}".format(t, not_gate(t)))

    # testing OR, NOR, AND, NAND and XOR gates

    inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]

    print ("\nOR gate \n")

    for t in range(len(inputs)):
        test = inputs[t]

        print ("OR  ({}, {}) = {}".format(inputs[t][0], inputs[t][1], or_gate(inputs[t])))

    print ("\nNOR gate \n")

    for t in range(len(inputs)):
        test = inputs[t]

        print ("NOR ({}, {}) = {}".format(inputs[t][0], inputs[t][1], nor_gate(inputs[t])))

    print ("\nNOR gate with NOT \n")

    for t in range(len(inputs)):
        test = inputs[t]

        print ("NOR ({}, {}) = {}".format(inputs[t][0], inputs[t][1], nor_gate_not(inputs[t])))    

    print ("\nAND gate \n")

    for t in range(len(inputs)):
        test = inputs[t]

        print ("AND ({}, {}) = {}".format(inputs[t][0], inputs[t][1], and_gate(inputs[t])))

    print ("\nNAND gate \n")

    for t in range(len(inputs)):
        test = inputs[t]

        print ("NAND ({}, {}) = {}".format(inputs[t][0], inputs[t][1], nand_gate(inputs[t])))

    print ("\nNAND gate with NOT \n")

    for t in range(len(inputs)):
        test = inputs[t]

        print ("NAND ({}, {}) = {}".format(inputs[t][0], inputs[t][1], nand_gate_not(inputs[t])))

    print ("\nXOR gate \n")

    for t in range(len(inputs)):
        test = inputs[t]

        print ("XOR ({}, {}) = {}".format(inputs[t][0], inputs[t][1], xor_gate(inputs[t])))
