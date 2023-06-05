try:
    largest = None
    smallest = None

    while True:
        numInput = input('Enter a number:')
        if numInput == 'done':
            break
        num = int(numInput)
        if  largest is None or num > largest:
            largest = num
        if smallest is None or smallest > num:
            smallest = num
    
    print(largest, smallest)

except:
    print('Invalid input')