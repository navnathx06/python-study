# Q. Write a program to find out whether a given post is talking about “navnath” or not.

post = input("Enter the post : ")

if("navnath".lower() in post.lower()):
     print("This post is talking about navnath")

else:
     print("This post is not talking about navnath")