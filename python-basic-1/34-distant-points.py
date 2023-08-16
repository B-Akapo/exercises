# Description: A program that calculates the distance between the points (x1, y1) and (x2, y2).

from math import sqrt, pow


def main():
    # Get coordinates from user input
    x1 = validate_input("Please enter a value for x1: ")
    x2 = validate_input("Please enter a value for x2: ")
    y1 = validate_input("Please enter a value for y1: ")
    y2 = validate_input("Please enter a value for y2: ")

    # Calculate and print the distance
    distance = calculate_distance(x1, x2, y1, y2)
    print("The distance between the points is:", distance)


def validate_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def calculate_distance(x1, x2, y1, y2):
    x_diff_squared = pow(x2 - x1, 2)
    y_diff_squared = pow(y2 - y1, 2)

    # Calculate and return the distance
    distance = sqrt(x_diff_squared + y_diff_squared)
    return distance


if __name__ == "__main__":
    main()
