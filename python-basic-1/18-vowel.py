# Decription: A program that checks if a letter passed is a vowel

"""
This program checks if a given letter is a vowel.

The program prompts the user to enter a single character and checks if the input is a single character. It then converts the input to lowercase and checks if it is one of the vowels 'a', 'e', 'i', 'o', or 'u'. If it is, it returns "Input is a vowel", otherwise it returns "Input is not a vowel".

Example Usage:
Please enter a single character: a
Input is a vowel
"""

def main():
    while True:
        try:
            user_input = input("Please enter a single character: ")
            if len(user_input) == 1:
                answer = vowel_check(user_input)
                print(answer)
                break
        except ValueError:
            print("Please enter a single character") 

def vowel_check(user_input):
    user_input = user_input.lower()  # Convert to lowercase
    if user_input in ['a', 'e', 'i', 'o', 'u']:
        return "Input is a vowel"
    else:
        return "Input is not a vowel"

if __name__ == "__main__":
    main()

