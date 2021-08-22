def miniMaxSum(arr):
    arr=list(sorted(set(arr)))
    min,max=0,0
    min,max = arr[0: len(arr) - 1], arr[1:]
    min,max = sum(min),sum(max)
    print(min,max)

miniMaxSum([5,3,1,7,9])
