#Python script for reading and printing(first column) csv file
import csv

with open('example1.csv', 'r') as file1:
    dsChar = csv.reader(file1)

    next(dsChar) #Skips the header

    print("Printing the first column:")
    for line in dsChar:
        print(line[0]) #Specifying which column to print

#Python script for reading and printing json file
import json

with open('example2.json', 'r') as file2:
    hpChar = json.load(file2)
    out = json.dumps(hpChar, indent=4)
   
    print("\nPrinting using load function:")
    print(hpChar)
    print("\nPrinting using dump function:")
    print(out)