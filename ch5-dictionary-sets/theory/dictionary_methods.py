marks = {
    "navnath":100,
    "om": 56,
    "raj" : 34,
    0 : "hii"

}

print(marks.items()) # Returns a list of (key,value)tuples.

print(marks.values())

print(marks.keys()) #Returns a list containing dictionary's keys.

marks.update({"navnath":99}) # update value
print(marks)

print(marks.get("navnath")) # Returns the value of the specified keys (and value is returned