import os
import time
import multiprocessing

def SumEven(no):
    
    print(f"PID of SumEven :{os.getpid()} PPID of Sumeven: {os.getppid()}")
    sum =0
    for i in range(2 , no , 2):
        sum = sum +i
        
    print("Summation of even :", sum)

def SumOdd(no):
    
    print(f"PID of SumOdd :{os.getpid()} PPID of SumOdd: {os.getppid()}")
    sum =0
    
    for i in range(1,no,2):
      sum = sum +i
        
    print("Summation of odd :", sum)
        
def main():
    
    start_time = time.perf_counter()
    
    t1 = multiprocessing.Process(target =SumEven , args=(100,))
    t2 = multiprocessing.Process(target =SumOdd , args=(100,))
    
    t1.start()
    t2.start()
    
    t1.join
    t2.join
    
    end_time = time.perf_counter()
    
    print(f"time required is :{end_time - start_time:.4}")
  
  
if __name__ == "__main__":
    main()