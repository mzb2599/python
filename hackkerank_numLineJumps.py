# You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

# The first kangaroo starts at location  and moves at a rate of  meters per jump.
# The second kangaroo starts at location  and moves at a rate of  meters per jump.
# You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO

def kangaroo(x1, v1, x2, v2):
    p = v1
    q = v2
    condition1 = 100000000
    condition2 = 100000000

    if((x2 > x1 and v2 > v1) or (x1 > x2 and v1 > v2)):
        return "NO"
    if(v1 < 1000 and v2 < 1000):
        condition1 = 100000
        condition2 = 100000

    while(v1 < condition1 and v2 < condition2):
        if(x1+v1 == x2+v2):
            return "YES"
        else:
            v1 += p
            v2 += q
    return "NO"


kangaroo(4523, 8092 ,9419, 8076)
