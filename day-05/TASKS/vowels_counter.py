# Write the code ↓ to prompt the user to enter a word.
# Be cautious when reading input of various data types.
print("VOWEL COUNTER FOR ALF\n")

userInput = input("Please enter a word/s to check: ")


# Write the code ↓ to count the number of vowels in the entered word.
# Utilize string functions to iterate through the characters and identify vowels.
vowelCount = 0
for i in userInput:
    if i in 'aeiouAEIOU':
        vowelCount += 1

# Write the code ↓ to display the count of vowels in the word.
# Select and employ a string concatenation method based on your personal preference and comfort level.
print("The number of vowels in '{}' is: {}".format(userInput, vowelCount))     
