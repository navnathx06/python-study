# append() -  adds element at the end of the list

a = ["apple","ball","cat","dog"]

print(a)
a.append("elephent") 
print(a)

# sort() - updates the list 

l1 = [4,6,8,2,1]
l1.sort()
print(l1)

# reverse() - reverse the list

l1 = [4,6,8,2,1]
l1.reverse()
print(l1)

# insert() - for add or insert element

b = [2,3,4,5,6,9]
b.insert(3,1) # agar bich mey kuch insert karna ho toh
print(b)

# pop - Will delete element at index  and return its value.

c = [3,4,6,7,9,2,1]
c.pop(2) # index 2 ka element delete ho jayega
print(c)

# remove() - use to remove element

d= [2,4,5,6,7,8]
d.remove(2)
print(d)