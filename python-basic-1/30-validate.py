# Description: A program that adds two objects if both objects are integers

def main():
    num1 = validate_input("Please enter an integer: ")
    num2 = validate_input("Please enter an integer: ")
    
    if num1 and num2:
        print("Both inputs are integers.")
    else:
        print("Both values must be integers.")

def validate_input(prompt):
    try:
        num = int(input(prompt))
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()
