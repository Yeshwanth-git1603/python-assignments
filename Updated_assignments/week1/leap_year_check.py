# write a python program to find whether a year is leap year or not

# Function to check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input a year
year = int(input("Enter a year: "))

# Check and display if the year is a leap year
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
