#Python program for encoding json file
import json

username = input("Enter your name: ")
age = int(input("Enter your age: "))
favfood = input("Enter your favorite food: ")

userData = {
    "Name" : username,
    "Age" : age,
    "Favorite Food" : favfood
}

content = json.dumps(userData, indent=2)

print(content)

with open('output.json', 'w') as file:
    file.write(content)
