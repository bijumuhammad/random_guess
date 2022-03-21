a=[]
val=int(input("enter a number : "))

for i in range(1,val):
    if(val%i)==0:
        a.append(i)
a.append(val)
print(a)
