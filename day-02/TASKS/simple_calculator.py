import sys
# Write the code ↓ to read user's input for two operands and selected operation.
# NOTE: The two operands must be read as floats.
print("SIMPLE CALCULATOR FOR ALF\n")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, x, /): ")

# Write the code ↓ to perform the calculations based on the selected operation.
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "x":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("\nEnter a valid operator from the choices only. Run the program again.")
    sys.exit()

# Write the code ↓ to display the result.
# Select and employ a string concatenation method based on your personal preference and comfort level.
print("\nThe result of {} {} {} is {}".format(num1, operator, num2, result))
