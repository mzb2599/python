# An English text needs to be encrypted using the following encryption scheme.
# First, the spaces are removed from the text. Let  be the length of this text.
# Then, characters are written into a grid, whose rows and columns have the following constraints:

# Example


# After removing spaces, the string is characters long. is between and, so it is written in the form of a grid with 7 rows and 8 columns

#https://www.hackerrank.com/challenges/encryption/problem

import math
def encrypt(s):
    a=[]
    count=0
    s=s.strip()
    for x in range(0, len(s)):
    #    print(s[x], end="")
        a.append(s[x])
        #count += 1
    v = math.sqrt(len(s))
    if(int(v)==v):
        r=int(v)
        c=int(v)
    else:
        r, c = int(v), int(v)+1
        #if(count==c):
        #     print("")
        #     count = 0
    #print(a)
    enc_s = ''
    itr=0
    for i in range(0, r):
        for j in a[i::c]:
            enc_s+=j    
        enc_s+=" "
    return enc_s

def encryption(s):
    a = []
    count = 0
    s = s.strip()
    for x in range(0, len(s)):
        #    print(s[x], end="")
        a.append(s[x])
        #count += 1
    v = math.sqrt(len(s))
    if (v != int(v)):
        r, c = int(v), int(v) + 1
    else:
        r = c = int(v)
            
    #if(count==c):
    #     print("")
    #     count = 0
    #print(a)
    enc_s = ''
    itr = 0
    for i in range(0, r):
        for j in a[i::c]:
            enc_s += j
        enc_s += " "
    return enc_s


print(encrypt("iffactsdontfittotheorychangethefacts"))

 