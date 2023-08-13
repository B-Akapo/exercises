# Description: A program that computes the greatest common divisor (GCD) of two positive integers. 

import math 

def main():
    num1 = int(input("Enter the first positive integer: "))
    num2 = int(input("Enter the second positive integer: "))
    
    lcm_result = calculate_lcm(num1, num2)
    print(f"The LCM of {num1} and {num2} is {lcm_result}")

def calculate_lcm(a, b):
    return math.lcm(a, b)

if __name__ == "__main__":
    main()
