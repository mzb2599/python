d = {}
n = int(input('Enter the number of elementrs to insert in  dictionary :'))
i = 0
for i in range(n):
    k = input('Enter the key: ')
    v = input('Enter the value: ')
    d.setdefault(k, v)
print(d)
d1=d.copy()
s = input('Enter the key to search corresponding value: ')
for k, v in d.items():
    if k == s:
        print(d[s])
dv = input('Enter the key to delete corresponding value: ')
for k, v in d.items():
     if k == dv:
         c = 1
         break
if c == 1:
    del d [dv]
print(d)


    
