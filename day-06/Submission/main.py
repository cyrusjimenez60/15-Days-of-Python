#Python program for reading and printing text file
file = open('example.txt','r')

writtenText = file.read()

print(writtenText) #Prints the file content

file.close()
