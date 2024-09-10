#python programs week1
# printing the numbers which are divisible by 5 and not a multiple of 11
# in the range of(1000,2000)

for x in range(1000,2000):
    if x%5==0 and x%11!=0:
        print(x,end=",")
