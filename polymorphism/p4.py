class Bird():
    def intro(self):
        print('Intro birds')
    def flight(self):
        print('Some birds cannot fly high')
class sparrow(Bird):
    def flight(self):
        print('Sparrrows can fly')
class ostrich(Bird):
    def flight(self):
        print('Ostrich cannot fly high')

B = Bird()
S = sparrow()
O = ostrich()

B.intro()
B.flight()

S.intro()
S.flight()

O.intro()
O.flight()
