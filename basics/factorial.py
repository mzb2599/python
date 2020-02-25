def factorial(n):
    f, i = 1, 1
    print(f,i,n)
    for i in range(n):
        f = f * i
        i += 1
    return f
n = int(input("Enter the number: "))
print(factorial(n))
'''
Enter the number: 5

'''