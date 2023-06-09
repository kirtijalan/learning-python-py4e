def chop(listSet) :
    del listSet[0]
    length = len(listSet)
    del listSet[length-1]

def giveMidItems(listSet) :
    length = len(listSet)
    newList = []
    for item in range(len(listSet)):
        if item == 0 or item == length-1 : continue
        newList.append(listSet[item])
    return newList


al = ['qwerty', 'uiop', 'asdf', 123]
print('new list:', giveMidItems(al))
# print('******')
chop(al)
print(al)

