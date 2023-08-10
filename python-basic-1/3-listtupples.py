# Description: A program  that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.

def main():
    user_input = input("Please enter a sequence of numbers separated by commas: ")
    list_conversion = convert_list(user_input)
    tuple_conversion = convert_tuple(user_input)
    print(list_conversion)
    print(tuple_conversion)

def convert_list(user_input):
    num_list = [int(num) for num in user_input.split(",")]  # Split using commas
    return num_list

def convert_tuple(user_input):
    num_tuple = tuple(int(num) for num in user_input.split(","))
    return num_tuple

if __name__ == "__main__":
    main()
