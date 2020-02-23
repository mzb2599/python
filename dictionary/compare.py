x=2
print(x.bit_length())
y = x.__sizeof__()
print('Size of integer is:', y)
x = 2.0
y = x.__sizeof__()
print('Size of integer is:', y)
x = 'Zaki'
y = x.__sizeof__()
print('Size of String is:', y)
