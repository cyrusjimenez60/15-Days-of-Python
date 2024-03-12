#Python program for reading and printing text file
file = open('example.txt','r')

writtenText = file.read()

print(file.read()) #Shortcut printing

file.close()
