# Description: A program to display the current date and time

import datetime

current_time = datetime.datetime.now().strftime("%H:%M:%S")
print("Current time:", current_time)


