#This program will calculate the hypotenuse from inputs
# @authors Sarah, Tyler, Lisa, James

from math import sqrt
#get the sides
sideOne = int(input("Leg one length: "))
sideTwo = int(input("Leg two lenght: "))

#calulate the hypoteuse
print("Hypotenuse: " , sqrt(sideOne ** 2 + sideTwo ** 2))