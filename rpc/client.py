import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
multicall = xmlrpc.client.MultiCall(proxy)
n1=float(input("Enter number 1:"))
n2=float(input("Enter number 2:"))
op=input("Enter the operation(+,-, *,/):")
if(op=='+'):
    multicall.add(n1, n2)
elif(op=='-'):
    multicall.subtract(n1, n2)
elif(op=='*'):
    multicall.multiply(n1, n2)
elif(op=='/'):
    multicall.divide(n1, n2)
    
# multicall.add(7, 3)
# multicall.subtract(7, 3)
# multicall.multiply(7, 3)
# multicall.divide(7, 3)
result = multicall()

#print("7+3=%d, 7-3=%d, 7*3=%d, 7//3=%d" % tuple(result))
print(str(n1)+" "+op+" "+str(n2)+"=")
print(list(tuple(result))[0])
