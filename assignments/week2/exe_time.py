#finding the execution time of a program using time module
import time

# Record the start time
start_time = time.time()

a,b=0,1
i=0
print("the fibanocci of the given number series  is:")
while i<5:
    a,b=b,a+b
    i+=1
    print(a,end=" ")
    print()
    
end_time=time.time()

execution_time = start_time - end_time

print(f"the time used for the program is {execution_time} seconds:")
    

