# calculating the sum of the digits of a number
import time
start_time=time.time()
number=int(input("enter the number"))
sum_of_digits=0
while number>0:
    last_digit=number%10
    sum_of_digits+=last_digit
    number=number//10

print("the sum of digits of a given number is:",sum_of_digits)
end_time=time.time()
execution_time=start_time-end_time
print(f"the time used for the program is {execution_time} seconds:")
