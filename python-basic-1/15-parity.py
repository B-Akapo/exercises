# Description: A program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user. 

def main():
    user_input = get_input()
    parity = parity_check(user_input)
    print(parity)

def get_input():
    try:
        prompt = int(input("Please enter a number: "))
    except ValueError:
        print("Please enter a number")
        return get_input()
    return prompt

def parity_check(prompt):
    if prompt % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == '__main__':
    main()