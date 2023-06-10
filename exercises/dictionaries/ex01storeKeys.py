# Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
# It doesn’t matter what the values are. 
# Then you can use the in operator as a fast way to check whether a string is in the dictionary.

import random

fname = input('Enter file name:')
theFile = open(fname)

newDict = dict()

for lines in theFile:
    words = lines.split()
    for word in words:
        newDict[word] = random.randint(0,9)

strCheck = input('Enter word to search:')
if strCheck in newDict:
    print('The word "%s" exists in the file.' % strCheck)
else:
    print('The word "%s" does not exist in the file.' % strCheck)

# print(newDict)
    


