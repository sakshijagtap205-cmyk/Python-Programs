no = 11                                           #Global Variable NO

def Display():                                    #function
  a =21                                           #local variable
  print("From Display,:", no)
  print("From Display value of a is :", a)
   

def Demo():                                        #function
    print("From Demo:", no)
    print("From Demo value of a is :", a)          #error

Display()                                          #function call
Demo()                                             #function call