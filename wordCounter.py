#! python3
# wordCounter.py - Asks the user for filename of file to open, then asks
# the user for a comma-separated list of words to match and once complete,
# prints a list of the words and their frequency in the file.

import re

def openFile():
    fileName = input("What is the name of the file you would like to open? ")
    try:
        fileHandler = open(fileName, "r+")  # opens file in read & write mode
        string = fileHandler.read()         # reads whole file into string
        fileHandler.close()                 # closes the file
        return string
    except OSError as e:
        print("No file named " + fileName + " was found in this directory.")

def wordCount(searchSplit, textSplit):
    count = 0

    for word in textSplit:
        if(word == searchSplit):
            count += 1
    return count

def stripNotWords(text):
    text = re.sub(r"\W+", " ", text)
    text = text.lower()
    return text

text = None
while(text == None):
    text = openFile()
text = stripNotWords(text)
textSplit = text.split(" ")
search = input("What words would you like to search for? ")
search = stripNotWords(search)
searchSplit = search.split(" ")
for i in range(0, len(searchSplit)):
    frequency = wordCount(searchSplit[i], textSplit)
    print("The word " + searchSplit[i] + " appeared " + str(frequency) + " times.")
