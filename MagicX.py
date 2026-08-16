class Demo:
    def __init__(self, A):
        self.No = A
        
    def __add__(Self , sakshi):
        return Self.No + sakshi.No
        
    def __sub__(Self , sakshi):
        return Self.No - sakshi.No
    
    def __mul__(Self , sakshi):
        return Self.No * sakshi.No
    
    def __truediv__(Self , Sakshi):
        return Self.No / Sakshi.No
    
        
obj1 = Demo(11)
obj2 = Demo(21)

print(obj1+obj2)   #obj1.___add__(Obj2) --> __add__(obj1, obj2)
print(obj1-obj2)   #obj1.___add__(Obj2) --> __sub__(obj1, obj2)
print(obj1*obj2)   #obj1.___add__(Obj2) --> __mul__(obj1, obj2)
print(obj1/obj2)   #obj1.___add__(Obj2) --> __truediv__(obj1, obj2)