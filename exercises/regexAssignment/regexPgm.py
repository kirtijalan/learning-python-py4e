import re

# fname = input('Enter file name:')
# dataSet = open(fname)

dataSet = open('actual.txt')

data = list()

for line in dataSet:
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        data.append(x)

total = 0
count = 0
for val in data:
    for num in val:
        count = count + 1
        total = total + int(num)


print('There are %d values and the sum=%d' % (count, total))

