mails = open('./../files/mbox.txt')
mailCount = 0
for lines in mails:
    if lines.startswith("From "):
        words = lines.split()
        mailCount = mailCount + 1
        print(words[1])

print('There are %d lines in the file with From as the first word' % mailCount)

    
