# Exercise 2: Write a program to look for lines of the form:
# New Revision: 39772
# Extract the number from each of the lines using a regular expression and the findall() method.
# Compute the average of the numbers and print out the average as an integer.


import re

fin = input('enter file:')

fileMap = None
if fin == 'mbox.txt':
    fileMap = './../files/mbox.txt'
else:
    fileMap = './../files/mbox-short.txt'

fout = open(fileMap)

data = list()

for line in fout:
    x = re.findall('^New Revision:*\s([0-9]+)', line)
    if len(x) > 0:
        # print(x)
        data.append(x)

dl = len(data)
# print('DL: ', dl)

count = 0

for val in data:
    # print(int(val[0]))
    count = count + int(val[0])

# print('data-count:', count)   

print(int(count/dl))



