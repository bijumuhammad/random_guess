from sys import flags


str=input("Enter a Word : ")
flag=0
for x in range (0,len(str)//2):
    if(str[x]!=str[len(str)-x-1]):
        flag=1
if(flag==0):
    print("pallindrome")
else:
    print("Not pallindrome")