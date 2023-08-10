# Description: A program  that accepts the user's first and last name and prints them in reverse order with a space between them 

def main():
    name = input("Enter first and last name: ")
    reversed_name = reverse_name(name)
    if reversed_name:
        print(reversed_name)
    else:
        print("Please enter both first and last names.")

def reverse_name(name):
    words = name.split()
    if len(words) >= 2:
        rearranged_name = words[1] + " " + words[0]
        return rearranged_name
    else:
        return None

if __name__ == "__main__":
    main()
