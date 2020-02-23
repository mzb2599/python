hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter the rate per hour")
rate = float(rate)
if hrs <= 40:
    Pay = hrs*rate
else:
    Pay = 40*rate+(hrs-40)*rate*1.5
print(Pay)

print(Pay)
