class Base:
    def __init__(self):
        print("Inside Base Constructure")
   
class Derived(Base): #python
    def __init__(self):
        super().__init__()
        print("Inside Derived Constructure")


dobj = Derived()