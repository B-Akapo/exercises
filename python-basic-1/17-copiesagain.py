# Description: A program that gets n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2. 

def main():
    user_input = input("Please enter a word: ")
    print_copies = make_copies()
    split_input = split_string(user_input, print_copies)
    print(split_input)

def split_string(user_input, print_copies):
    if len(user_input) < 2:
        return user_input * print_copies
    else:
        return user_input[:2] * print_copies

def make_copies():
    i = 0
    while i < 3:
        try:
            copies = int(input("Please enter the number of copies: "))
            if copies >= 0:
                return copies
            else:
                raise ValueError("Please enter a non-negative integer!!")
        except ValueError:
            raise ValueError("Please enter a number!!")
        i += 1
    raise Exception("Too many attempts. Exiting program.")

if __name__ == "__main__":
    main()
