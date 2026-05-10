import random
'''
snake = 1
water = -1
gun = 0

'''

computer = random.choice([-1,0,1]) # used to choose random number

youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1: "snake",-1:"water",0:"gun"}

youstr = input("Enter your choice (s/w/g): ").lower()

if youstr not in youDict:
    print("Invalid choice")
    exit()

you = youDict[youstr]

print(f"You chose: {reverseDict[you]}" )
print(f"computer chose: {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer == -1 and you == 1):
        print("You Win!")

    elif(computer == -1 and you == 0):
        print("You Lose!")

    elif(computer == 1 and you == -1):
        print("You Lose!")

    elif(computer == 1 and you == 0):
        print("You Win!")

    elif(computer == 0 and you == -1):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You Lose!")

    else:
        print("something went wrong!")