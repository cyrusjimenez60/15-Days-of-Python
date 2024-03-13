#Python script that asks and writes the user's name
file = open('user_info.txt','w')

username = input("Enter your name: ")

file.write(username)

file.close()
