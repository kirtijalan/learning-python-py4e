#pay computation 
#give the employee 1.5 times the hourly rate for hours worked above 40 hours.
hours = input('Enter Hours:')
rate = input('Enter Rate:')
if int(hours) > 40:
    # pay = (int(40) * float(rate)) + ((int(hours)-40)* 1.5 *float(rate))
    pay = float(rate) * ( int(40) + (int(hours)-40) * 1.5 ) #simplified version of above commented code
else: 
    pay = int(hours) * float(rate)
print('Pay:', pay)

