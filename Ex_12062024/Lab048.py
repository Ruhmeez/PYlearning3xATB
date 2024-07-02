# age = 90
#
# if age > 100:
#     print("You are old")

# 1. Leap Year Checker:
# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also
# divisible by 400.
# Use an if-else statement to make this determination.
# Input = 2024
# Output = Leap year
#____________________________________

Y = 2024

if Y/4 == 0:
    print("Its Leap year")
    if Y/100 != 0:
        print("Its not leap year")
