'''
r  -> read
w  -> write
a  -> append
x  -> create new file
b  -> binary mode
t  -> text mode

'''

# r mode -> read file
f = open("file.txt", "r")
print(f.read())
f.close()


# w mode -> write file 
f = open("file.txt", "w")
f.write("Hello")
f.close()

# a mode -> append data
f = open("file.txt", "a")
f.write("\nNew Line")
f.close()

# x mode -> create new file
f = open("newfile.txt", "x")
f.close()

# rb mode -> read binary file
f = open("image.jpg", "rb")
print(f.read())


# wb mode -> write binary file
f = open("data.bin", "wb")
f.write(b"Hello")
f.close()