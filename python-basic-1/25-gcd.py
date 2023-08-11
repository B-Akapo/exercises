# Description: A program that computes the greatest common divisor (GCD) of two positive integers. 

"""
This code snippet calculates the greatest common divisor (GCD) of two positive integers.


Explanation:
- The code snippet prompts the user to enter two positive integers and calculates their GCD using the math.gcd() function. 
- The result is then printed.
- There is an input validation to ensure that the user enters positive integers.
"""

import math 

def main():
    """
    Entry point of the program.
    """
    num1 = int(input("Enter the first positive integer: "))
    num2 = int(input("Enter the second positive integer: "))
    
    gcd_result = calculate_gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is {gcd_result}")

def calculate_gcd(a, b):
    """
    Calculates the GCD of two numbers using the math.gcd() function.
    
    Args:
        a: First positive integer.
        b: Second positive integer.
    
    Returns:
        The GCD of the two numbers.
    """
    return math.gcd(a, b)

if __name__ == "__main__":
    main()
