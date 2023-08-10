# Description: A program that returns a string that is n (non-negative integer) copies of a given string. 

def main():
    word = input("Please enter a word: ")
    copies = get_copies()
    copies_made = make_copies(word, copies)
    print(copies_made)

def get_copies():
    while True:
        try:
            copies = int(input("Please enter the number of copies: "))
            if copies >= 0:
                break
            else:
                print("Please enter a non-negative integer!!")
        except ValueError:
            print("Please enter a number!!")
    return copies

def make_copies(word, copies):
    return word * copies

if __name__ == "__main__":
    main()