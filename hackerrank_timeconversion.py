def timeConversion(s):
    t = s.split(':')
    #print(t)
    temp = t[2][2]
    x=t[0]
    if(temp == 'P'):
        if(t[0] != '12'):
            x = int(t[0])+12
    else:
        if t[0] == '12':
            x = 0
    if(int(x) == 0):
        t[0] = '0'+str(x)
    else:
        t[0] = str(x)
    time = ''
    for x in t:
        time += x[0:2]+':'
    time = time[:-1]
    print(time)
    return time


timeConversion('12:40:22AM')
