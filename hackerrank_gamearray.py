def gamingArray(arr):
    f = bool(False)
    while(len(arr) > 0):
        l = 0
        for x in arr:
            if x > l:
                l = x
        #print(l, arr.index(l))
        index = arr.index(l)
        for i in range(index, len(arr)):
            arr.pop()
        f = not(f)
        print(f)

    if(f):
        return "BOB"
    else:
        return "ANDY"

def GA(arr):
    a=list()
    l = arr[0]
    a.append(l)
    for x in arr:
        if (x > l):
           a.append(x)
    print(a) 

#https: // www.hackerrank.com/challenges/an-interesting-game-1/problem?h_r = next-challenge & h_v = zen & h_r = next-challenge & h_v = zen
GA([5 ,2, 6, 3 ,4])
