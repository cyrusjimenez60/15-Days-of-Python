# Write the code ↓ to prompt the user to enter a word.
# Be cautious when reading input of various data types.
print("PALINDROME CHECKER FOR ALF\n")

word = input("Please, enter a word/s to check: ")

# Write the code ↓ to check if the entered word is a palindrome.
# Utilize string functions to compare the original word with its reverse.
loweredCaseWord = word.lower()
reversedWord = loweredCaseWord[::-1]

# Write the code ↓ to display whether the entered word is a palindrome or not.
# Select and employ a string concatenation method based on your personal preference and comfort level.
if reversedWord == loweredCaseWord:
    print("'{}' is a palindrome.".format(word))
else:
    print("'{}' is not a palindrome.".format(word))
