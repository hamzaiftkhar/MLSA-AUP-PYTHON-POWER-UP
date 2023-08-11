#Python Program to check the Range of  number provided by user

# Take the input from the user:
num = int(input("Enter the number: "))

# Check the range of the number:

if num < 0 or num > 100:
    print("The number is out of range")
elif num > 0 and num < 11:
    print("Low range number")
elif num > 10 and num < 51:
    print("Medium range number")
elif num > 50 and num < 101:
    print("High range number")
else:
    print("The number is out of range")                