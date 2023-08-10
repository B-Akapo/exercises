# Description: A program that calculate the sum of three given numbers. If the values are equal, return three times their sum. 

NUM_INPUTS = 3  # Number of inputs to be provided

def main():
    user_inputs = [] 
    for i in range(NUM_INPUTS):
        prompt = f"Please enter number {i + 1}: "
        user_input = get_user_input(prompt)
        user_inputs.append(user_input)
    answer = calculate_sum(*user_inputs)
    print("The calculated sum is:", answer)
def get_user_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def calculate_sum(num1, num2, num3):
    total_sum = num1 + num2 + num3
    if num1 == num2 == num3:
        return 3 * total_sum
    else:
        return total_sum
    
if __name__ == "__main__":
    main()

