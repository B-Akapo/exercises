# Description: A program that calculates the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference. 


def main():
    try:
        user_input = int(input("Please enter a number: "))
        
        # Call the function to calculate the difference
        constant = 17
        diff = calculate_difference(user_input, constant)
        
        if user_input > constant:
            # Double the difference if the input number is greater than the constant
            result = 2 * diff
        else:
            result = diff
        
        print("Result:", result)
        
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def calculate_difference(number, constant):
    return abs(constant - number)

if __name__ == "__main__":
    main()




