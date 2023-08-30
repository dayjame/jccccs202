# Program to convert inches to Yards/Feet/Inches
# @authors Sarah, Tyler, Lisa, James
# Our not so magic numbers
YARDS = 36
FEET = 12

#Get inches
inches = int(input("Number of inches: "))

#Convert to Yd Ft In
yard = inches // YARDS
inches = inches % YARDS
feet = inches // FEET
inches = inches % FEET

#Print
print(f"{yard} Yards \n{feet} Feet \n{inches} Inches")