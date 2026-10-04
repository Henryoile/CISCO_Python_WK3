# 3.1.6   LAB   Variables ‒ Questions and answers
n = int(input("Enter a number: "))
print(n >= 100)


# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one
largest_number = number1

# We check if the second nubmer is larger than the current largest number
# and update the largest_number if needed
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than the current largest number
# and update the largest_number if needed
if number3 > largest_number:
    largest_number = number3

# Print the results
print("The largest number is: ", largest_number)