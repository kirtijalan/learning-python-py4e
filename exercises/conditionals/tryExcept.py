#pay computation 
#give the employee 1.5 times the hourly rate for hours worked above 40 hours.
#Rewrite your pay program using try and except so that your program handles non-numeric input gracefully
try:
    hours = input('Enter Hours:')
    hrs = int(hours)
    rate = input('Enter Rate:')
    rt = float(rate)
    if int(hours) > 40:
        # pay = (int(hours) * float(rate)) + ((int(hours)-40)* 1.5 *float(rate))
        pay = rt * ( hrs + (hrs-40) * 1.5 )
    else: 
        pay = hrs * rt
    print('Pay:', pay)
except:
    print('please enter a numeric input')

#expected output is 475.0
