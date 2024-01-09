import time
from calendar import isleap


# Function to judge if a year is a leap year
def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False


# Function to return the number of days in each month considering leap years
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28


# User input for name and age
name = input("input your name: ")
age = input("input your age: ")

# Get the current local time
localtime = time.localtime(time.time())

# Convert age to years, months, and days
year = int(age)
month = year * 12 + localtime.tm_mon
day = 0

# Calculate the starting and ending year for the age calculation
begin_year = int(localtime.tm_year) - year
end_year = begin_year + year

# Calculate the total days considering leap years
for y in range(begin_year, end_year):
    if judge_leap_year(y):
        day = day + 366
    else:
        day = day + 365

# Check if the current year is a leap year
leap_year = judge_leap_year(localtime.tm_year)

# Calculate the days for the months completed in the current year
for m in range(1, localtime.tm_mon):
    day = day + month_days(m, leap_year)

# Add the days of the current month
day = day + localtime.tm_mday

# Display the result
print("%s's age is %d years or " % (name, year), end="")
print("%d months or %d days" % (month, day))
