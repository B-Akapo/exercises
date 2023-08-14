# Description: A program that sums three given integers. However, if two values are equal, the sum will be zero. 

def main():
    num1 = validate_input("Enter the first positive integer: ")
    num2 = validate_input("Enter the second positive integer: ")
    num3 = validate_input("Enter the third positive integer: ")

    result = calculate_sum(num1, num2, num3)
    print(result)

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

def calculate_sum(a, b, c):
    if a == b or b == c or a == c:
        return 0
    else:
        return a + b + c

if __name__ == "__main__":
    main()
