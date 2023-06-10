# Exercise 2: 
# Write a program that categorizes each mail message by which day of the week the commit was done. 
# To do this look for lines that start with “From”, 
# then look for the third word and keep a running count of each of the days of the week. 
# At the end of the program print out the contents of your dictionary (order does not matter).

# fname = input('Enter file name:')
# mails = open(fname)
mails = open('./../files/mbox-short.txt')
countWeekDays = dict()
for lines in mails:
    if lines.startswith("From "):
        words = lines.split()
        weekDay = words[2]
        countWeekDays[weekDay] = countWeekDays.get(weekDay,0) + 1
        
print(countWeekDays)
    
