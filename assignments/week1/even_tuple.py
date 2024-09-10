# creating a tuple and adding the even numbers into it
list1=[]
for x in range(1,20):
    if x % 2 == 0:
        list1.append(x)
print(list1)
t1=tuple(list1)
print(t1)
print(type(t1))
