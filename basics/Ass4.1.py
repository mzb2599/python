def computepay(h, rate):
    if hrs <= 40:
   		Pay = hrs*rate
    else:
        Pay = 40*rate+(hrs-40)*rate*1.5
    return Pay

hrs = input("Enter Hours:")
p = computepay(10,20)
print("Pay",p)
