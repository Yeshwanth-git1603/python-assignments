# finding the factors of the number

number=int(input("enter the number"))
list1=[]
for x in range(1,10):
    if number % x == 0:
        list1.append(x)
        
print(list1)


