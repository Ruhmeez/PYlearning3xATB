#Take the 2 int number from the user and we want to add them.
#we need to use the input() function

num1 = input("enter the first number: ")
num2 = input("enter the second number: ")
result = num1+num2
print(result)

num1 = input("enter the first number: ")
num2 = input("enter the second number: ")
#type conversion - str->int->int()
result = int(num1)+int(num2)
print(result)

#+ ->int sum operator
#+ -> str - concat
#int to str -> str()
#str to int -> int()

print(type(int(num1)))