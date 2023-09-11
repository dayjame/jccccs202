"""This program displays a sphere diameter, surface area,
and volume based off user-entered data
@author James Day"""

from math import pi

# Get the radius
radius = float(input("Sphere radius: "))

# Compute and display the diameter, surface area, and volume
print(f"Diameter: {2 * radius:,.2f} units")
print(f"Surface area: {4 * pi * pow(radius, 2):,.2f} square units")
print(f"Volume {4 / 3 * pi * pow(radius, 3):,.2f} cubic units")