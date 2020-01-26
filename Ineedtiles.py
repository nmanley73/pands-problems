# Program calculates tiles required when tiling a wall (m2)

length = float(input("Enter room length"))
width = float(input("Enter room width"))

#length = 3.5
#width = 2.4

area = length * width

needed = area * 1.05

print("you need", needed, "tiles in metres squared.")

