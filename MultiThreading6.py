import time
def SumEven(no):
    sum =0
    
    for i in range(2 , no , 2):
        sum = sum +i
        
    print("Summation of even :", sum)

def SumOdd(no):
    
    sum =0
    
    for i in range(1,no,2):
      sum = sum +i
        
    print("Summation of odd :", sum)
        
def main():
    
    start_time = time.perf_counter()
    SumEven(100000000)
    SumOdd(100000000)
    
    end_time = time.perf_counter()
    
    print(f"time required is :{end_time - start_time:.4}")
  
  
        
if __name__ == "__main__":
    main()