f_set = {1,2,3,4,6,3,5,3,2,4}
print(f_set)

#remove duplicates in list with set
l1 =[12,34,12,1,4,1,3,5,2,78,9,4,97,7]
print(list(set(l1)))

# common values in both sets
set1 = {1,6,8,9,4,5,99,67}
set2 = {9,8,6,3,2,5,1,4}
common = set(set1) & set(set2)
print(common)

common_set = set1.intersection(set2)
print(common_set)

set1.intersection_update(set2)
print(set1)

set1.add(87)
print(set1)
print(set2.copy())

diff_set = set1.difference(set2)
print(diff_set)

set2.difference_update(set1) 
print(set2)

set1.discard(4)
print(set1)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple","cherry"}

x.update(y) 
print(x)

z = x.union(y)
print(z)

z = x.symmetric_difference(y) 
print(z)

x.symmetric_difference_update(y)
print(x)

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)
print(z)
z = x.issubset(y)
print(z)
z = y.issubset(x)
print(z)

p = {"a", "b", "c"}
q = {"ae", "be", "ce","a"}
print(q.isdisjoint(p))