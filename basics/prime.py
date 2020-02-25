n = int(input("Enter the number"))
c=0
if n > 1:
    for i in range(2, n - 1):
        if n % i == 0:
            c = 1
            break
        else:
            continue
if c == 1:
    print(n, 'is not a prime number')
else:
    print(n,'a prime no')