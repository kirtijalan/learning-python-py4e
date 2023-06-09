numList = []
while True:
    numInput = input('Enter a number:')
    if numInput == 'done':
        break
    try:
        num = float(numInput)
    except:
        print('Invalid input')
        continue
    
    numList.append(numInput)


print('Maximum:', max(numList))
print('Minimun:', min(numList))