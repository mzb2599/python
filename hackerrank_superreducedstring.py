def superReducedString(s):
    t = ''
    i=0
    while (i < len(s) - 1):
        a = s[i]
        b = s[i+1]
        if(a == b):
            i+=2
        else:
            t += s[i]
            i += 1
    if(len(s) % 2 != 0):
        t+=s[len(s)-1]
    return t


print(superReducedString('baab'))
