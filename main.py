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


# Tax calculator
income = float(input("Enter the annual income: "))

if income < 85528:
	tax = income * 0.18 - 556.02
else:
	tax = (income - 85528) * 0.32 + 14839.02

if tax < 0.0:
	tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "Shillings")


# 3.2.4   LAB   Guess the secret number
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

guess = int(input("Enter a number: "))

while guess != secret_number:
    print("Ha ha! you are stuck in my loop!")
    guess = int(input("Enter a number: "))
    
print(guess)
print("Well done, muggle! you are free now.")

# 3.2.7   LAB   Essentials of the for loop – counting mississippily
import time
for i in range (1, 6):
    print(i, "mississippi")
    time.sleep(1)

print("Ready or not, here I come!")


# 3.2.9   LAB   The break statement – Stuck in a loop

while True:
    word = input("Enter a word: ")
    if word == "chupacabra":
         print("You've successfully left the loop.")
         break


# 3.2.10   LAB   The continue statement – the Ugly Vowel Eater

# Ask for the word and convert it to uppercase
user_word = input("Enter a word: ")
user_word = user_word.upper()

# Loop through each letter in the word
for letter in user_word:
     if letter == "A":
          continue
     elif letter == "E":
          continue
     elif letter == "I":
          continue
     elif letter == "O":
          continue
     elif letter == "U":
          continue
     else:
        print(letter)


# 3.2.14   LAB   Essentials of the while loop

blocks = int(input("Enter the number of blocks: "))

height = 0
layer = 1

while blocks >= layer:
     blocks -= layer
     height += 1
     layer += 1

print("The height of the pyramid: ", height)







