import time
import threading

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
    
    t1 = threading.Thread(target =SumEven , args=(10000000,))
    t2 = threading.Thread(target =SumOdd , args=(10000000,))
    
    t1.start()
    t2.start()
    
    t1.join
    t2.join
    
    end_time = time.perf_counter()
    
    print(f"time required is :{end_time - start_time:.4}")
  
  
if __name__ == "__main__":
    main()