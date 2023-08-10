# Description: A program that gets the volume of a sphere with radius six

from math import pi

def main():
    radius = float(input("Enter the value of the radius: "))
    answer = calculate_volume(radius)
    print(f"Area of the circle = {answer}")

def calculate_volume(radius):
    volume = (4/3) * pi * (radius ** 3)
    return volume

if __name__ == "__main__":
    main()

