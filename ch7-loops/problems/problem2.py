# Q. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
# l = ["Navnath", "Soham", "Sachin", "Rahul"]

l = ["Navnath", "Soham", "Sachin", "Rahul"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")


'''
output

Hello Soham
Hello Sachin

'''