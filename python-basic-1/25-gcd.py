# Description: A program that computes the greatest common divisor (GCD) of two positive integers. 

import math  
def main():
    num1 = int(input("Enter the first positive integer: "))
    num2 = int(input("Enter the second positive integer: "))
    
    gcd_result = calculate_gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is {gcd_result}")

def calculate_gcd(a, b):
    return math.gcd(a, b)

if __name__ == "__main__":
    main()
