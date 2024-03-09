# Write the code ↓ to read the user's input for a positive integer.
# Be cautious when reading input of various data types.
print("PERFECT NUMBER DETERMINATOR FOR ALF\n")

while (True):
    num = int(input("Please enter a positive integer: "))
    if num > 0:
        break
    else:
        print("Please enter a non-negative integer only. Try again.\n")

# Write the code ↓ to check if the entered integer is a Perfect Number using a loop.
sum = 0
for i in range(1, num, 1):
    if (num % i) == 0:
        sum += i
                
# Write the code ↓ to display the Perfect Number check result.
# NOTE : You can use if-else statement or ternary operator to display the result.
if sum == num:
    print(f"{num} is a Perfect Number")
else:
    print(f"{num} is not a Perfect Number")
