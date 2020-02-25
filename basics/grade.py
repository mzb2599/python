n = (int)(input('Enter the percentage'))
if n>100 or n<0:
    print('Invalid input')
elif n > 80:
    print('A grade')
elif n>60:
    print('B grade')
elif  n>=40:
    print('Pass')
else:
    print("Fail")
