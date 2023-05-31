from carfailure import model

print ("Car failure \n")

# calculate probability of given observations (evidences)

probability = model.probability([["no electronic failure", "no mechanic failure", "car works"]])
print ("P(no electronic failure, no mechanic failure, car works)", probability)

probability = model.probability([["no electronic failure", "mechanic failure", "car works"]])
print ("P(no electronic failure, mechanic failure, car works)", probability)

probability = model.probability([["electronic failure", "mechanic failure", "car works"]])
print ("P(electronic failure, mechanic failure, car works)", probability)

# calculate probability of car failure

car_probability = 0

probability = model.probability([["electronic failure", "mechanic failure", "car does not work"]])
car_probability += probability

probability = model.probability([["electronic failure", "no mechanic failure", "car does not work"]])
car_probability += probability

probability = model.probability([["no electronic failure", "mechanic failure", "car does not work"]])
car_probability += probability

probability = model.probability([["no electronic failure", "no mechanic failure", "car does not work"]])
car_probability += probability

print ("")

print("car failure probability", car_probability)

# calculate probability of no car failure

car_probability = 0

probability = model.probability([["electronic failure", "mechanic failure", "car works"]])
car_probability += probability

probability = model.probability([["electronic failure", "no mechanic failure", "car works"]])
car_probability += probability

probability = model.probability([["no electronic failure", "mechanic failure", "car works"]])
car_probability += probability

probability = model.probability([["no electronic failure", "no mechanic failure", "car works"]])
car_probability += probability

print ("no car failure probability", car_probability)

# predictions

print ("\nprediction: no car failure \n")

predictions = model.predict_proba({
    "car_failure": "car works"
})

for node, prediction in zip(model.states, predictions):
    if isinstance(prediction, str):
        print(f"{node.name}: {prediction}")
    else:
        print(f"{node.name}")
        for value, probability in prediction.parameters[0].items():
            print(f"    {value}: {probability:.4f}")

print ("\nprediction: car does not work \n")

predictions = model.predict_proba({
    "car_failure": "car failure"
})

for node, prediction in zip(model.states, predictions):
    if isinstance(prediction, str):
        print(f"{node.name}: {prediction}")
    else:
        print(f"{node.name}")