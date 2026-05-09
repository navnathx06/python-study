# Q. Write a program to calculate the factorial of a given number using for loop.

# 5! = 5 X 4 X 3 X 2 X 1 = 120

n = int(input("Enter the number: "))
product = 1
for i in range(1, n+1):
    product = product * i

print(f"The factorial of {n} is {product}")

'''
output

Enter the number: 5
The factorial of 5 is 120

'''