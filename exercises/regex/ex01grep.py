import re

pattern = input('Enter a regular expression:')
selFile = open('./../files/mbox.txt')

count = 0
# regexp = pattern + '.'
# print(regexp)
for line in selFile:
    if re.search(pattern, line):
        count = count + 1
        # print(pattern)

print('mbox.txt had %d lines that matched %s' % (count, pattern))
