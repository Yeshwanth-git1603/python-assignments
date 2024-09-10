# finding the most common element in the list and how many times it has occured

from collections import Counter

list1=[1,2,3,4,5,6,7,3,4,22,4,2]

counter = Counter(list1)

most_frequent=counter.most_common(1)[0]

print(f"the most common number is {most_frequent[0]} and it occured {most_frequent[1]} times")
