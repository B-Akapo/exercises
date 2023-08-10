# Description: A program that gets a newly-generated string from a given string where "Is" has been added to the front. 
# Return the string unchanged if the given string already begins with "Is". 

def main():
    user_input = input("Enter a word: ")
    modified_word = add_is_prefix(user_input)
    print(modified_word)

def add_is_prefix(word):
    if word.lower().startswith("is"):
        return word
    else:
        return "Is" + word

if __name__ == "__main__":
    main()
