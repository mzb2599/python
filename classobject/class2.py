class Dog:
    kind = 'Bull dog'
    def __init__(self, name):
        print('Instance created of type dog')
        self.name = name
d = Dog('Trump')
print(d.kind)
d.kind = 'German Shepherd'
print('Type :', d.kind)
print('Name :', d.name)
