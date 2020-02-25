n = int(input("Enter the number"))
terms = int(input("Enter the power"))
result = list(map(lambda x: n ** x, range(terms)))
print("The total terms is:", terms)
for i in range(terms):
   print(n," raised to power", i, "is", result[i])
'''
Output:
c:\Users\MOHD ZAKI\Desktop\Sem4\python\college\exp3>py lamda.py
Enter the number3
Enter the power3
The total terms is: 3
3  raised to power 0 is 1
3  raised to power 1 is 3
3  raised to power 2 is 9
'''