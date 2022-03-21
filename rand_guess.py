import random
val=int(input("enter the guess number from 0 to 10 "))
rand=random.randrange(0,10)
print("The random number is",rand)
if(val==rand):
    print("Congrats ,right guess")
else:
    if(val<rand):
        print("The guess is lower")
    else:
        print("the guess is higher")