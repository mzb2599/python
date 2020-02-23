boys = ['Musharaf', 'Aun']
girls = ['Alfiya', 'Uzma']
vl = boys, girls
print(vl)
# l = boys + girls
# print(l)
girls[1] = 'Zainab'
print(vl)
others = []
nw = vl, others
print(nw)
t = boys, girls, others
print(t)