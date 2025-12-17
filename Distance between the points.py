x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

dx = x2 - x1
dy = y2 - y1

distance = (dx*dx + dy*dy) ** 0.5

print("Distance between the points =", distance)
