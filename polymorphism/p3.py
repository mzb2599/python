#paranthesis are used for inheritance
class India():
    def __init__(self):
        print("Constructor-India")
    def capital(self):
        print('New Delhi')
    def language(self):
        print('Hindi')

class Usa():
    def __init__(self):
        print("Constructor-Usa")
    def capital(self):
        print('New York')
    def language(self):
        print('English')
ind = India()
Us = Usa()
for details in (ind, Us):
    details.capital()
    details.language()


    
    
    
