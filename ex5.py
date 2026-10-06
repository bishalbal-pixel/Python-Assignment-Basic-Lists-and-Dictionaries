numbers = [12, 5, 8, 20, 15, 3, 10]

# 1. Ask the user to enter a number
num = int(input("Enter a number: "))

# 2 & 3. Check and print a message
if num in numbers:
    print(num, "is present in the list.")
else:
    print(num, "is not present in the list.")