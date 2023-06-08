fname = input("Enter file name: ")
spamTotal = 0
count = 0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    spamConf = float(line[20:].strip())
    spamTotal = spamTotal + spamConf
    avg = spamTotal/count

print('Average spam confidence:', avg)