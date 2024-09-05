# sets 

set1={1,2,3,4,5,6,32,22,11,22,12,334,22344,22343}
print(set1)
set1.add(10)
print(set1)
set1.remove(22343)
print(set1)
set1.remove(22344)
print(set1)
# frozen set
# cant make changes to this set
#because it changed as frozen set

s=frozenset(set1)
print(s)

