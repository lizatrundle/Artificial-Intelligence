from classattendance import model

print ("Rain, traffic, and class attendance \n")

# calculate probability of given observations (evidences)

probability = model.probability([["no rain", "traffic jam", "bus on time", "attend on time"]])
print ("P(no rain, traffic jam, bus on time, attend on time)", probability)

probability = model.probability([["light rain", "no traffic jam", "bus on time", "attend on time"]])
print ("P(light rain, no traffic jam, bus on time, attend on time)", probability)

probability = model.probability([["light rain", "traffic jam", "bus delayed", "attend on time"]])
print ("P(light rain, traffic jam, bus delayed, attend on time)", probability)

probability = model.probability([["light rain", "no traffic jam", "bus delayed", "attend delayed"]])
print ("P(light rain, no traffic jam, bus delayed, attend delayed)", probability)

# predictions

print ("\nheavy rain \n")

predictions = model.predict_proba({
    "rain": "heavy rain"
})

for node, prediction in zip(model.states, predictions):
    if isinstance(prediction, str):
        print(f"{node.name}: {prediction}")
    else:
        print(f"{node.name}")
        for value, probability in prediction.parameters[0].items():
            print(f"    {value}: {probability:.4f}")


print ("\nlight rain \n")

predictions = model.predict_proba({
    "rain": "light rain"
})

for node, prediction in zip(model.states, predictions):
    if isinstance(prediction, str):
        print(f"{node.name}: {prediction}")
    else:
        print(f"{node.name}")
        for value, probability in prediction.parameters[0].items():
            print(f"    {value}: {probability:.4f}")


print ("\nlight rain, no traffic jam \n")

predictions = model.predict_proba({
    "rain": "light rain", "traffic": "no traffic jam",
})

for node, prediction in zip(model.states, predictions):
    if isinstance(prediction, str):
        print(f"{node.name}: {prediction}")
    else:
        print(f"{node.name}")
        for value, probability in prediction.parameters[0].items():
            print(f"    {value}: {probability:.4f}")


print ("\nlight rain, no traffic jam, bus delayed \n")

predictions = model.predict_proba({
    "rain": "light rain", "traffic": "no traffic jam", "bus": "bus delayed"
})

for node, prediction in zip(model.states, predictions):
    if isinstance(prediction, str):
        print(f"{node.name}: {prediction}")
    else:
        print(f"{node.name}")
        for value, probability in prediction.parameters[0].items():
            print(f"    {value}: {probability:.4f}")
