# Description: A Program that returns true if the two given integer values are equal or their sum or difference is 5. 

def main():
    num1 = validate_input("Please enter the first integer: ")
    num2 = validate_input("Please enter the second integer: ")
    answer = check_sum(num1, num2)
    print(answer)

def validate_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Please enter a valid integer.")

def check_sum(a, b):
    if a == b or a + b == 5 or a - b == 5:
        return True
    else:
        return False

if __name__ == "__main__":
    main()