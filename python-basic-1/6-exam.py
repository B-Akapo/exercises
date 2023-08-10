# Description: A program that display the examination schedule. (extract the date from exam_st_date).

from datetime import datetime

def main():
    exam_st_date = "11, 12, 2014"
    date_format = "%d, %m, %Y" # specify the format of the date

    # convert to date format
    try:
        convert_date = datetime.strptime(exam_st_date, date_format)
        date_object = convert_date.date()  # Remove the time part
        print("Date object:", date_object)
    except ValueError as e:
        print("Error:", e)
    
if __name__ == "__main__":
    main()

