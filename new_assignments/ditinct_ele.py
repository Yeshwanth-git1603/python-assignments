"""
# distinct elements in the list
def distinct_list():
    list1=list(input("enter the numbers:"))
    list2=[]
    for x in list1:
        if x not in list2:
            list2.append(x)
    print(list2)
        
distinct_list()
