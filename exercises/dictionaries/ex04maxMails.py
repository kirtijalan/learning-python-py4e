# Exercise 4: Add code to the above program to figure out who has the most messages in the file. 
# find who has the most messages and print how many messages the person has.

# Exercise 3: Write a program to read through a mail log, 
# build a histogram using a dictionary to count how many messages have come from each email address, 
# and print the dictionary.

mailLog = open('./../files/mbox.txt')
mailIDs = dict()
for line in mailLog:
    if line.startswith('From '):
        words = line.split()
        mailIDs[words[1]] = mailIDs.get(words[1], 0) + 1

# print(mailIDs)


maxMails = None
sender = None
for k in mailIDs:
    if maxMails == None or mailIDs[k] > maxMails:
        maxMails = mailIDs[k]
        sender = k

print(sender, maxMails)