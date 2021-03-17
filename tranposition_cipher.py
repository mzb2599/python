import numpy as np
l = list()
m=list()
def transp_cipher(text):
    l=list()
    for alphabet in text:
        l.append(alphabet)
    length = len(l)
    #Fix length to divisible of 5
    while length % 5 != 0:
        l.append("$")
        length=len(l)
    array = np.array(l)
    array = np.reshape(array, (-1, 5))
    print("Before transpose: \n",array)
    array = np.transpose(array)
    print("After transpose: \n",array)
    cipher=""
    for x in array:
        for y in x:
            cipher=cipher+y
    return cipher


def transp_decipher(text):
    m=list()
    for alphabet in text:
        m.append(alphabet)
    leng=len(m)
    arr = np.array(m)
    
    dim = int(len(m) / 5)
    
    arr = np.reshape(arr, (-1, dim))
    arr = np.transpose(arr)
    decipher=""
    for x in arr:
        for y in x:
            if y == "$":
                continue
            decipher = decipher + y
    
    return decipher


 