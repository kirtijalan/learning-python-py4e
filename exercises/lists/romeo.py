txtFile = open('romeo.txt')
uniqueWords = []
for lines in txtFile:
    words = lines.split()
    for word in words:
        # print(word)
        if word not in uniqueWords:
            uniqueWords.append(word)
        
uniqueWords.sort() 
print(uniqueWords)