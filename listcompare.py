from sys import flags


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,34]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,89,34,89]

c=[]
for i in a:
      for j in b:
          if(i==j):
              if i not in c:
                  c.append(i)
print(c)