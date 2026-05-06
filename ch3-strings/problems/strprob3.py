# Write a program to detect double space in a string.

a = "i am a good boy" # return -1 because double space nhi hai
print(a.find("  "))
print(a.find("goo"))# kuch bhi find kr sakte

b = "i am a  good boy" # return index because isme double space hai
print(b.find("  "))