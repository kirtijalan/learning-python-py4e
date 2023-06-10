# Exercise 3: This program records the domain name (instead of the address) 
# where the message was sent from instead of who the mail came from (i.e., the whole email address). 
# At the end of the program, print out the contents of your dictionary.

mailLog = open('./../files/mbox-short.txt')
domainCount = dict()
for line in mailLog:
    if line.startswith('From '):
        words = line.split()
        domainName = words[1].split('@')[1]
        domainCount[domainName] = domainCount.get(domainName, 0) + 1

print(domainCount)
