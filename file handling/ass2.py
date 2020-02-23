# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
add = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    add = add+float(line[21:])
    count = count+1
    avg = add/count
print("Average spam confidence:", avg)
