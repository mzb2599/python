class Person:
    def __init__(self, id, name):
        self.id = id
        self.name=name
        print("Inside constructor\n","id:", id, "name:", name)
        print("Constructor ends")

#Creating object of class Person
p=Person(1,"Mohd Zaki")
print("Id:", p.id)
print("Name:", p.name)
print("__sizeof__:",p.__sizeof__)
