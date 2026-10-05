# 3.1.6   LAB   Variables ‒ Questions and answers
n = int(input("Enter a number: "))
print(n >= 100)

# 3.1.6   LAB   Variables ‒ Questions and answers

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




# 3.1.10   LAB   Comparison operators and conditional execution

# Read plant name
name = input("Enter plant name: ")

# Check the right plant name which is "Spythophyllum" with capital "S"
if name == "Spythophyllum":
    print("Spythophyllum is the best plant ever!")

# Check if the condition for capital "S" is not met.
elif name == "spythophyllum":
    print("No, I want a big Spythophyllum!")

# Anything else, echo the input back to the user
else:
    print("Spyhtophyllum! Not", name + "!")
