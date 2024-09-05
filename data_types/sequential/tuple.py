#tuple data type

t=(1,2,3,4,5)
print(t)
print(type(t))
#accessign the element using index
print(t[0])
# tuple is immutable and hence it doesnot allow insertion of values
print(t)
# the only way is to change the tuple type to list and then we can make insertions into it
l=list(t)
print(l)
l.append(6)
print(l)
t1=tuple(l)
print(t1)

