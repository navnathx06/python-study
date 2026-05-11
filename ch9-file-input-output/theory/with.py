f = open("file.txt")
print(f.read())
f.close()

#The sa,e can be written using with statement like this:
with open("file.txt") as f:
   print(f.read())

# You dont need to close the the file