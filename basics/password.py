import random,string
def password(x,y):
    a="".join(random.sample(string.ascii_lowercase,4))
    print(a)

password()