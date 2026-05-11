f = open("file.txt")

lines = f.readlines()
print(lines, type(lines))

# line1 = f.readlines()
# print(line1, type(line1))

f.close()