# Description: A program that checks if a file exists

import os.path

def main():
    user_input = input("Please enter file name: ")
    if check_file(user_input):
        print(f"{user_input} exists")
    else:
        print(f"{user_input} does not exist")

def check_file(user_input):
    if os.path.isfile(user_input):
        return True
    else:
        return False

if __name__ == "__main__":
    main()

