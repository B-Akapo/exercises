# Description: A program that checks whether a specified value is contained within a group of values

def main():
    user_input = get_valid_input()
    result = check_list(user_input)
    print(result)

def get_valid_input():
    while True:
        try:
            return int(input("Please enter a number: "))
        except ValueError:
            print("Please enter a valid number")

def check_list(user_input):
    my_list = [1, 5, 8, 3]
    return user_input in my_list

if __name__ == "__main__":
    main()
