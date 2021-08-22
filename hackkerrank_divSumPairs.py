def divisibleSumPairs(n, k, ar):
    t = []
    for x in ar:
        i = 0
        for y in ar[ar.index(x):]:
            if((x+y) % k == 0):
                t.append([x, y])
    t.sort()
    print(t)
    print(len(t))

    while(t[i]):
        if (t[i] == t[i + 1]):
            t.remove(t[i])
        i+=1
    print(t)
        

divisibleSumPairs(6, 3, [1 ,3 ,2 ,6 ,1 ,2])
