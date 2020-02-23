def hello():
    print('Hello')
    return('world')


hello()
h = hello
h()
print(h)
print(h())
