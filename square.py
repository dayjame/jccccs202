# Calculate the perimeter and area of a square
# @author James Day

# input length and width
length = int(input("Length:"))
width = int(input("Width: "))

# Calculate the perimeter 2*l + 2*w
perimeter = 2 * (length + width)

# Calculate the Area l * w
area = length * width

# Output area and perimeter
print(f"Area: {area} Perimeter: {perimeter}")
