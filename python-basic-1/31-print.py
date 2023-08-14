# Description: A program that displays your name, age, and address on three different lines. 

def main():
    print_info()

def print_info():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    address = input("Enter your address: ")
    
    info = f"{name}\n{age}\n{address}"
    print(info)

if __name__ == "__main__":
    main()

