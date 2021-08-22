def staircase(n):
    for k in range(n):
        for i in range(n-k):
            print(" ",end="")
        for j in range(n-i):
            print("#",end="")
        print("")
staircase(6)