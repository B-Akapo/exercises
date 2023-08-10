# Description: A program that calculates the area of a circle based on the radius entered by the user. 

from math import pi

def main():
    radius = float(input("Enter the value of the radius: "))
    answer = calculate_area(radius)
    print(f"Area of the circle = {answer}")

def calculate_area(radius):
    area = pi * (radius ** 2)
    return area

if __name__ == "__main__":
    main()



