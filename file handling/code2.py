fh = open("file1.txt", "r")
counter = 0
for line in fh:
    print(line.strip())
    counter = counter + 1
print(counter,'lines')
