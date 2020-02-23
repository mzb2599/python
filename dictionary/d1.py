tel = {'aiman': 9619, 'Moin': 5242, 'Zaki': 88212}
print(tel)
tel['aiman'] = 98927
print(tel['aiman'])
#print(tel['aim'])
tel['Mohd'] = 88792
print(tel)
print(list(tel))
tel=sorted(tel)
print(tel)
print('aiman' in tel)
print('Salik' not in tel)
# for x,y in tel.items():
#     print(x,y)
ls=['Mohd','Zaki','Bhojani']
for i, v in enumerate(ls):
    print(i,v)
for i, v in enumerate(tel):
    print(i+1, v)
        
