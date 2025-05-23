import math

def calculate_distance(x1, y1, x2, y2):  # Fixed function name
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

dist = calculate_distance(x1, y1, x2, y2)  # Fixed function call
print(f"Distance between the points: {dist:.2f}")
