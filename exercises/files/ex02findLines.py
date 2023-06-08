fileName = input('Enter the file name:')
data = open(fileName)
spamTotal = 0
count = 0
for line in data:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        spamConf = float(line[20:].strip())
        spamTotal = spamTotal + spamConf

print(spamTotal/count)
