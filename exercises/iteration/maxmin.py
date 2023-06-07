largest = None
smallest = None
while True:
    numInput = input('Enter a number:')
    if numInput == 'done':
        break
    try:
        num = int(numInput)
    except:
        print('Invalid input')
        continue

    if  largest is None or num > largest:
        largest = num
    if smallest is None or smallest > num:
        smallest = num

print('Maximum is', largest)
print('Minimum is', smallest)
