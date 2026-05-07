# Student marks dictionary
students = {
    "Navnath": 85,
    "Amit": 78,
    "Suresh": 90
}

# 1. get() → safe access (no crash if key missing)
print(students.get("Navnath"))     # 85
print(students.get("Ravi", 0))     # 0 (default value)

# 2. keys() → get all student names
print(students.keys())

# 3. values() → get all marks
print(students.values())

# 4. items() → key-value pairs (best for looping)
for name, marks in students.items():
    print(name, "scored", marks)

# 5. update() → add new student or update existing
students.update({"Ravi": 88})
students.update({"Amit": 80})   # overwrites Amit's marks

print(students)

# 6. setdefault() → add only if key not present
students.setdefault("Karan", 70)   # added
students.setdefault("Amit", 100)   # NOT changed

print(students)

# 7. pop() → remove specific student
removed_marks = students.pop("Suresh")
print("Removed Suresh marks:", removed_marks)

# 8. popitem() → removes last inserted item
last_item = students.popitem()
print("Last removed:", last_item)

# 9. copy() → create a shallow copy
new_students = students.copy()
print("Copied dict:", new_students)

# 10. clear() → remove all data
students.clear()
print("After clear:", students)