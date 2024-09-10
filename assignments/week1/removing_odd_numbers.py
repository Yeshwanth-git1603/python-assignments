# writing a program to remove all the odd number from the list
# here we are using lambda filter function

list3=[1,2,3,4,5,6,7,8,9,10]
result=list(filter(lambda x : True if x%2==0 else False,list3))
print(result)
