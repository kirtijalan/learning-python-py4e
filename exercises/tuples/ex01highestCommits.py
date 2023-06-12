# Exercise 1: Revise a previous program as follows: 
# Read and parse the “From” lines and pull out the addresses from the line. 
# Count the number of messages from each person using a dictionary.
# After all the data has been read, 
# print the person with the most commits by creating a list of (count, email) tuples from the dictionary. 
# Then sort the list in reverse order and print out the person who has the most commits.

# fh = input('Enter a file name:')
emailFile = open('./../files/mbox.txt')
# commitCount = 0
commitHist = dict()
for line in emailFile:
    if line.startswith('From '):
        words = line.split()
        commitHist[words[1]] = commitHist.get(words[1], 0) + 1

# print(commitHist)

data = list()
for (email, count) in list(commitHist.items()):
    data.append((count, email))

data.sort(reverse=True)

for count, email in data[0:1]:
    print(email, count)

