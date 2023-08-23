''' This program determins how many slices of pizza each person in a group may eat
@author James Day'''

#Get number of slices and people
numSlices = int(input("How many slices of pizza? "))
numPeople = int(input("How many people are eating? "))

#Deternube the number of slices for each person
slicesPerPerson = numSlices / numPeople

#Display the number of slices per person
print()
print(f"Number of slices per person {slicesPerPerson}")