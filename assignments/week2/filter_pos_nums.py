# filtering positive numbers from a list
# using filter function

nums=[1,2,3,-0,90,45,-34,2,-87,-56,-3,-2,-1,0,98,45]
result=list(filter(lambda x: True if x>0 else False,nums))
print(result)
