# If we specify ending="Thank you" in the line containing def, this value is used when no argument is passed.

def goodDay(name, ending="Thank you"):
    print(f"Good Day, {name}")
    print(ending)
# function body
goodDay("Navnath", "Thanks")
goodDay("Om" )# ending will be "Thank you" in function body (default)

'''
output

Good Day, Navnath
Thanks
Good Day, Om
Thank you

'''