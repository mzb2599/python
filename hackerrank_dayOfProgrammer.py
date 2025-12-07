def dayOfProgrammer(year):
    a=b=c=0
    if(year%400==0):
        a=1
    if(year%4==0):
        b=1
    if(year%100!=0):
        c=1
    
    if(a==1 or (b==1 and c==1)):
        return "12.09."+str(year)
            
    return "13.09."+str(year)
    
dayOfProgrammer(1800)