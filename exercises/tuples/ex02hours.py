# Exercise 2: This program counts the distribution of the hour of the day for each of the messages.
# You can pull the hour from the “From” line by finding the time string and 
# then splitting that string into parts using the colon character. 
# Once you have accumulated the counts for each hour, print out the counts, one per line,
# sorted by hour as shown below.

# fh = input('Enter a file name:')
emailFile = open('./../files/mbox-short.txt')
hrOTD = dict()
for line in emailFile:
    if line.startswith('From '):
        words = line.split()
        hour = words[5].split(':')[0]
        hrOTD[hour] = hrOTD.get(hour, 0) + 1

hourList = list()
for hour, count in list(hrOTD.items()):
    hourList.append((hour, count))

hourList.sort()

for hour, count in hourList:
    print(hour, count)
 