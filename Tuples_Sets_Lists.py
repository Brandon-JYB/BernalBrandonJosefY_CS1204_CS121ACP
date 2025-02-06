#TUPLES

mtup = 1,2,3
ytup = 'x', 'y', 'z'

xyup =mtup+ytup

retup = xyup * 5


print(retup)

print(2 in retup)
print(0 in retup)

tup = 1,2,3

x, y, z = tup

print(x)

print(y)

print(z)

#SETS

set= {1,2,3}

set.add(4)
print(set)

set.update([5,6,7])
print(set) 

set.remove(6)
print(set)

set.discard(3)
print(set)

pop= set.pop()
print(set)

set1= {1,2,3,4,5}
set2= {2,3,4,6}
set3= {1,2}

dif=set1.difference(set2)
print(dif)

inter=set1.intersection(set2)
print(inter)

union=set1.union(set2)
print(union)

sym=set1.symmetric_difference(set2)
print(sym)

#All elements of set 1 is in set 3
print(set1.issubset(set3))
#All elements of set 3 is in set 1
print(set1.issuperset(set3))

