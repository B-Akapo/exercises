# Description: A program that computes the future value of a specified principal amount, rate of interest, and number of years. 

def main():
    principal = validate_input("Please enter the principal amount: ")
    rate = validate_input("Please enter the annual rate of interest: ")
    time = validate_input("Please enter the time (in years): ")

    answer = calculate_future_value(principal, rate, time)
    print(answer)

def validate_input(prompt):
    while True:
        try:
            num = float(input(prompt))
            if num < 0:
                raise ValueError("Please enter a positive value")
            else:
                return num 
        except ValueError:
            print("Please enter a valid float")

def calculate_future_value(principal, rate, time):
    compound_interest = principal * (1 + ((rate/100))) ** (time)
    return round(compound_interest,2)

if __name__ == "__main__":
    main()


