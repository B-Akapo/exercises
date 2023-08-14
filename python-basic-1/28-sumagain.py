# Description: A program that sum two given integers. However, if the sum is between 15 and 20 it will return 20. 

def main():
    num1 = validate_input("Enter the first positive integer: ")
    num2 = validate_input("Enter the second positive integer: ")

    result = calculate_sum(num1, num2)
    print(result)

def validate_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num  # Add this line to return the valid input
        except ValueError:
            print("Please enter a valid integer.")

def calculate_sum(a, b):
    total = a + b
    if 15 <= total <= 20:  # Corrected the condition here
        return 20
    else:
        return total

if __name__ == "__main__":
    main()
