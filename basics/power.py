num = int(input("Enter the number of which you have to find power: "))
p = int(input("Enter the power: "))

k = 1
while p>0:
    k = num * k
    p-=1
print(k)
