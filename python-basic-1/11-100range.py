# Description: A program that tests whether a number is within 100 of 1000 or 2000


def main():
    try:
        user_input = int(input("Please enter a number: "))
        threshold = 100
        
        if abs(1000 - user_input) <= threshold:
            print(f"{user_input} is within {threshold} of 1000")
        elif abs(2000 - user_input) <= threshold:
            print(f"{user_input} is within {threshold} of 2000")
        else:
            print(f"{user_input} is not within {threshold} units of 1000 or 2000")
            
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()


