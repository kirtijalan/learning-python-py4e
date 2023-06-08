fileName = input('Enter the file name:')
data = open(fileName)
for word in data:
    print(word.upper())
