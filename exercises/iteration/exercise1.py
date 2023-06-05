try:
    count = 0
    total = 0

    while True:
        numInput = input('Enter a number:')
        if numInput == 'done':
            break
        num = int(numInput)
        count = count +1
        total = total + num

    avg = total/count
    print(total, count, avg)
except:
    print('Invalid input')



