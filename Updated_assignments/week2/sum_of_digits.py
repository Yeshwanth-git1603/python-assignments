# write a program to find the sum of the digits of a given number


number=int(input("enter the number"))
sum_of_digits=0
while number>0:
    last_digit=number%10
    sum_of_digits+=last_digit
    number=number//10

print("the sum of digits of a given number is:",sum_of_digits)
