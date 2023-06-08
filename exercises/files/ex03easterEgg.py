fileName = input('Enter the file name:')
count = 0
try:
    data = open(fileName)
except:
    if fileName == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punkedd!')
    else:
        print('File cannot be opened:', fileName)
    quit()

for line in data:
    if line.lower().startswith('subject'):
        count = count + 1

print('There were %d subject lines in %s' % (count, fileName))
