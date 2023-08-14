# Description: A program program to solve (x + y) * (x + y)

def main():
    x = validate_input("Please enter  the value of x: ")
    y = validate_input("Please enter  the value of y: ")
    answer = solve_equation(x, y)
    print(f"(4 + 3) ^ 2) = {answer}")

def validate_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Please enter a valid integer!")

def solve_equation(x, y):
    solution = ((x + y) ** 2)
    return solution

if __name__ == '__main__':
    main()