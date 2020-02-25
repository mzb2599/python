s = set()
n=int(input('Enter the number of elements'))
i = 0
for i in range(n):
    v=input('Enter the elements')
    s.add(v)
print(s)
s=sorted(s)
print(s)
for x in s: