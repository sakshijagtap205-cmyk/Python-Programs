import sys

if(len(sys.argv)== 3):
    
    no1 = int(sys.argv[1])   #int is typecast()
    no2 = int(sys.argv[2])    

    Ans = no1 + no2

    print("Addition is :", Ans)

else:
    print("Invalid number of arguments")