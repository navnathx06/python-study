# Write a program to input eight numbers from the user and display all the unique numbers (once).

s = set()

n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))

print(s)

# output :

# Enter number : 1
# Enter number : 2
# Enter number : 3
# Enter number : 3
# Enter number : 4
# Enter number : 4
# Enter number : 5
# Enter number : 6 
# {1, 2, 3, 4, 5, 6}