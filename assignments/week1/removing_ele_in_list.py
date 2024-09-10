# deleting the element in the list
# we can do by using pop()
# we can do by using remove()

list2=[1,2,3,4,5,6,7,8,9,9]
#deleting the element in the index 5
list2.pop(5)
print(list2)
list2.remove(9)
print(list2)
# if we use the pop() function without passing any parameter it defaultly deletes the element in the last index
list2.pop()
print(list2)
