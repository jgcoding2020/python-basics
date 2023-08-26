# Import necessary modules
import datetime
import time
from dateutil import relativedelta

# Current Date and Time
current_datetime = datetime.datetime.now()
print("Current Date and Time:", current_datetime)

# Date and Time Components
current_date = current_datetime.date()
current_time = current_datetime.time()
print("Current Date:", current_date)
print("Current Time:", current_time)

# Date Formatting
formatted_date = current_date.strftime("%Y-%m-%d")
print("Formatted Date:", formatted_date)

# Time Formatting
formatted_time = current_time.strftime("%H:%M:%S")
print("Formatted Time:", formatted_time)

# Parsing Date and Time
date_str = "2023-08-25"
parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
print("Parsed Date:", parsed_date)

# Adding and Subtracting Time
one_day = datetime.timedelta(days=1)
one_week = datetime.timedelta(weeks=1)
next_week = current_datetime + one_week
yesterday = current_datetime - one_day
print("Next Week:", next_week)
print("Yesterday:", yesterday)

# Unix Timestamp
timestamp = int(time.mktime(current_datetime.timetuple()))
print("Unix Timestamp:", timestamp)

# Date Difference
date1 = datetime.date(2023, 8, 25)
date2 = datetime.date(2023, 9, 1)
date_difference = date2 - date1
print("Date Difference:", date_difference)

# Date Comparison
if date2 > date1:
    print("Date2 is later than Date1")

# Date Arithmetic with dateutil.relativedelta
date3 = datetime.date(2023, 12, 31)
date4 = datetime.date(2024, 2, 29)
delta = relativedelta.relativedelta(date4, date3)
print("Date Arithmetic with relativedelta:")
print("Years Difference:", delta.years)
print("Months Difference:", delta.months)
print("Days Difference:", delta.days)
