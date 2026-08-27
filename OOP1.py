class Demo:
    #class Variable
    Value1 = 10
    Value2 = 20
    
    def __init__(self):
        #Instance Variable
        self.no1 = 11
        self.no2 = 21
        
        #Instance Method
    def fun(self):
        print("Inside Instance method name as fun")
        print(self.no1)
        print(self.no2)
        print(self.Value1)
        print(self.Value2)
        
dobj = Demo()
dobj.fun()
