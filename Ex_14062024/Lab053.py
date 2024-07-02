# Multiple conditions
# Swith in Java
# in python we have "Match Case" - works only on latest version of python
# (v3.10 n more)

# example2
# numbers = int(input("Enter a number\n"))
# match numbers:
#     case 1:
#         print("You have entered 1")
#     case 2:
#         print("You have entered 2")
#     case 3:
#         print("You have entered 3")
#     case 4:
#         print("You have entered 4")
#     case 5:
#         print("You have entered 5")
#     case _:
#         print("No idea")

# example1
# names = input("Enter a name\n")
# match names:
#     case "Ruheen":
#         print("You are Ruheen")
#     case "Firdos":
#         print("You are Firdos")
#     case _:
#         print("No idea")


# example3
browser = str(input("Enter the browser name\n"))
browser = browser.lower()
match browser:
    case "chrome":
        print("Chrome code executed")
    case "firefox":
        print("Firefox code executed")
    case _:
        print("No browser found")
