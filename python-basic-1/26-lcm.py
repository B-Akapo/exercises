# Description: A program that computes the greatest common divisor (GCD) of two positive integers. 

import math 

def main():
    num1 = validate_input("Enter the first positive integer: ")
    num2 = validate_input("Enter the first positive integer: ")
    
    lcm_result = calculate_lcm(num1, num2)
    print(f"The LCM of {num1} and {num2} is {lcm_result}")

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

def calculate_lcm(a, b):
    return math.lcm(a, b)

if __name__ == "__main__":
    main()
