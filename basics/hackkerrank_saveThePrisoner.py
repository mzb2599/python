 
def saveThePrisoner(n, m, s):
    if(m+s<=n):
        print(n,m,s)    
        return m+s-1
    else:

        for i in range(1,m):
            if(s<n):
                s+=1
            else:
                s=1
            print(n,m,s)    
        return s

print(saveThePrisoner(3,7,3))