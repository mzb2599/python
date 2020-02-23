fh = open('file1.txt')
for line in fh:
    if line.startswith('Read'):
        print(line)
#Extra line is due to 2 "\n" of file and print.        
fh = open('file1.txt')
for line in fh:
    if line.startswith('Read'):
        line=line.rstrip()
        print(line)
