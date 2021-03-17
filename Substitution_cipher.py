import numpy as np
table=dict()
tab=dict()
for x in range(26):
    table[x] = chr(65 + x)
    tab[chr(65 + x)] =x

def subst_cipher(text, key):
    l = ""
    for alphabet in text:
        if alphabet == ".":
            l=l+alphabet
        elif alphabet!=" ":
            alphabet=alphabet.upper()
            #Equivalent number (m)
            d = tab[alphabet]
            #add key(m+k)
            d = d + key
            #mod 26   (m+k)mod26
            d = d % 26
            #Equivalent cipher text
            d = table[d]
            #Concetanate str
            l = l +  d
        else:
            l=l+alphabet
    return l

def plain_text(text, key):
    dec_text = ""
    for alphabet in text:
        if alphabet == ".":
            dec_text = dec_text+alphabet
        elif alphabet != " ":
            alphabet = alphabet.upper()
            c = tab[alphabet]
            #C+26-K
            c = c + 26 - key
            #mod 26
            c = c % 26
            #decrypted text
            dec_text = dec_text + table[c]
        elif alphabet == " ":
            dec_text = dec_text + alphabet
    return dec_text
