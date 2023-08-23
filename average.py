'''Calculate the average of 5 numbers
@author James Day'''

#Get the 5 numbers
numOne = int(input("Number One: "))
numTwo = int(input("Number Two: "))
numThree = int(input("Number Three: "))
numFour = int(input("Number Four: "))
numFive = int(input("Number Five: "))

#Add the 5 numbers
sumNum = numOne + numTwo + numThree + numFour + numFive

#Average the numbers
avgNum = sumNum / 5

#Print the average
print(f"The average of the 5 numbers is {avgNum}")