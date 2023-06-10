# Exercise 3: Write a program to read through a mail log, 
# build a histogram using a dictionary to count how many messages have come from each email address, 
# and print the dictionary.

mailLog = open('./../files/mbox-short.txt')
mailIDs = dict()
for line in mailLog:
    if line.startswith('From '):
        words = line.split()
        mailIDs[words[1]] = mailIDs.get(words[1], 0) + 1

print(mailIDs)
