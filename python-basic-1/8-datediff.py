from datetime import datetime

def main():
    first_date_str = "2014, 7, 1"
    second_date_str = "2014, 7, 11"
    date_format = "%Y, %m, %d"  # specify the format of the date

    try:
        first_date = datetime.strptime(first_date_str, date_format).date()
        second_date = datetime.strptime(second_date_str, date_format).date()
        print("First Date:", first_date)
        print("Second Date:", second_date)

        # Calculate the difference between the dates
        difference_days = (second_date - first_date).days
        print(f"The difference in dates is {difference_days} days")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()