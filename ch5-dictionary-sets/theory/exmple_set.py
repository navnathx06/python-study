# Create a set
s = {1, 2, 3, 4}
print("Original set:", s)

# add() → adds single element
s.add(5)
print("After add(5):", s)

# update() → adds multiple elements
s.update([6, 7])
print("After update([6,7]):", s)

# remove() → removes element (error if not present)
s.remove(3)
print("After remove(3):", s)

# discard() → removes element (no error if not present)
s.discard(10)  # 10 not present, no error
print("After discard(10):", s)

# pop() → removes random element
removed = s.pop()
print("Popped element:", removed)
print("After pop():", s)

# copy() → creates a copy
s_copy = s.copy()
print("Copied set:", s_copy)

# clear() → removes all elements
temp = {100, 200}
temp.clear()
print("After clear():", temp)


# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

# union → combine all unique
print("Union:", a.union(b))

# intersection → common elements
print("Intersection:", a.intersection(b))

# difference → a - b
print("Difference (a-b):", a.difference(b))

# symmetric_difference → non-common elements
print("Symmetric Difference:", a.symmetric_difference(b))


# Relation methods

# issubset()
print("a subset of b?:", a.issubset(b))

# issuperset()
print("a superset of b?:", a.issuperset(b))

# isdisjoint()
print("a disjoint with {10,20}?:", a.isdisjoint({10, 20}))