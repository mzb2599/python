colour = []
colour = ['Yellow', 'Black']
print(colour)
colour[1] = 'Red'
print(colour)
x = 5
colour.append(x)
print(colour)
#deep copy
newcolours = ['green', 'blue']
newcolours = colour + newcolours
print(newcolours)
#shallow copy
print(newcolours + ['White'])
print(newcolours)
colour.clear()
print(colour)
