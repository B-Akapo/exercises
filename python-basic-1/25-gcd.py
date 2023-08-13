# Description: A program that computes the greatest common divisor (GCD) of two positive integers. 

import math

def main():
    num1 = validate_input("Enter the first positive integer: ")
    num2 = validate_input("Enter the second positive integer: ")
    
    gcd_result = calculate_gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is {gcd_result}")

def validate_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num <= 0:
                print("Please enter a positive integer.")
            else:
                return num
        except ValueError:
            print("Please enter a valid integer.")

def calculate_gcd(a, b):
    return math.gcd(a, b)

if __name__ == "__main__":
    main()
