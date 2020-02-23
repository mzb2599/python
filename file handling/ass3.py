fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    if line.split() not in lst:
    	lst.append(line.split())
print(lst)
