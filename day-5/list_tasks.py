from functools import reduce
l1 = [1, 2, 3, 5, 8,8,9,1,5,3, 9]
# list sum with reduce method
print(reduce(lambda x, y: x + y, l1)) 
# sum with for loop
total_sum = 0
for i in l1:
    total_sum += i
print(total_sum)

# mul with reduce method
print(reduce(lambda x,y:x*y,l1))

#  with max method
print(max(l1))
# find max with sort 
l2 = sorted(list(set(l1)))
print(l2[-1])
# find max with for loop
max_val = l1[0]
for i in l1:
    if i > max_val:
        max_val = i
print(max_val)   

#remove duplicates with set
l3 = list(set(l1))
print(l3)
#remove duplicates with for loop
new_l1 = []
for i in l1:
    if i not in new_l1:
        new_l1.append(i)
print(new_l1)        

#reverse list
l1.reverse()
print(l1)


#second largest num
l2 = sorted(list(set(l1)), reverse = True)
print(l2[1])