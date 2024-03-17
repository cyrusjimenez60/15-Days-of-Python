#Python script for counting lines in a file

with open('story.txt', 'r') as file:
    content = file.readlines()
    lineCount = len(content)
   
    print("Number of lines in 'story.txt' file: {}".format(lineCount))
