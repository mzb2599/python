def add(x, y, z=0, v=1):
    return x + y + z+v


def add(x, y, z=5, v=10): #Function overwrites the previous function add
    return x + y + z+v


print(add(2, 3))
print(add(2, 3, 5))
