# Q. Write a program to print multiplication table of n using for loops in reversed order.

n = int(input("Enter a number: "))

for i in range(1,11):
    print(f"{n} X {11 -i} = {n*(11-i)}")

'''
output

Enter a number: 5
5 X 10 = 50
5 X 9 = 45
5 X 8 = 40
5 X 7 = 35
5 X 6 = 30
5 X 5 = 25
5 X 4 = 20
5 X 3 = 15
5 X 2 = 10
5 X 1 = 5

'''