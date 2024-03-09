# Write the code ↓ to read the user's input for a non-negative integer.
# Be cautious when reading input of various data types.
print("FACTORIAL CALCULATOR FOR ALF\n")

num = int(input("Please enter a non-negative integer: "))

# Write the code ↓ to calculate the factorial of the user-defined integer using a loop.
result = 1
for i in range(1, num + 1, 1):
    result *= i

# Write the code ↓ to display the factorial result.
# Select and employ a string concatenation method based on your personal preference and comfort level.
print("The factorial of {} is {}".format(num, result))
