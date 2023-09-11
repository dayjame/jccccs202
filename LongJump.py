"""This program converts a long jump given in
centimeters to feet and inches
@author James Day"""

CMS_PER_INCH = 2.54
INCHES_PER_FEET = 12

# Get the name and distance
firstName = input("Long jumper's first name: ")
lastName = input("Long jumper's last name: ")
distance = int(input("Distance jumped (cm): "))

# Convert to feet and inches
inches = distance // CMS_PER_INCH
feet = inches // INCHES_PER_FEET

# Display the conversion