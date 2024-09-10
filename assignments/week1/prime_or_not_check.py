# checking whether a number is prime or not

x=int(input("enter the number"))
i=0
c=0

for i in range(1,x+1):
    z=x%i
    if (z==0):
        c+=1
if (c==2):
    print("number is prime")
else:
    print("number is not prime")
