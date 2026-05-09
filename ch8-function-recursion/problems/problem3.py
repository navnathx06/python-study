# Q. How do you prevent a python print() function to print a new line at the end.

print("a")
print("b")
print("c", end="") # end="" used to avoid space
print("d", end="")

'''
output

a
b
cd
'''