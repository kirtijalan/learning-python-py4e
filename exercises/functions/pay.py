def payroll(hours, rate):
    #give the employee 1.5 times the hourly rate for hours worked above 40 hours.
    if int(hours) > 40:
        # pay = (int(40) * float(rate)) + ((int(hours)-40)* 1.5 *float(rate))
        pay = rate * ( int(40) + (hours-40) * 1.5 ) #simplified version of above commented code
    else: 
        pay = hours * rate
    return pay


hours = input('Enter Hours:')
rate = input('Enter Rate:')

print('Pay:', payroll(float(hours), float(rate)))