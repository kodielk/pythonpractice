import sys
import math

def calculate_radius(x1, y1):
    '''calculates radius'''
    return math.sqrt(x1**2 + y1**2)

def calculate_area(radius):
    '''calculates area given the radius'''
    return math.pi * radius**2

def calculate_circumference(radius):
    '''calculates circumference given the radius'''
    return 2 * math.pi * radius

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 elise_cobabe_function_advanced.py [radius/area/circum] x1 y1")
        sys.exit(1)

    choice = sys.argv[1]
    x1 = float(sys.argv[2])
    y1 = float(sys.argv[3])

    if choice == "radius":
        radius = calculate_radius(x1, y1)
        print(f"radius: {radius}")
    elif choice == "area":
        radius = calculate_radius(x1, y1)
        area = calculate_area(radius)
        print(f"area: {area}")
    elif choice == "circum":
        radius = calculate_radius(x1, y1)
        circum = calculate_circumference(radius)
        print(f"Circumference: {circum}")
    else:
        print("invalid choice. Choose 'radius', 'area', or 'circum'.")
        sys.exit(1)