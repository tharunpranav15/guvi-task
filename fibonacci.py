a=int(input("Enter a number:"))
b=[0,1,1]
for i in range(2,a-1):
     c=b[i-1]+b[i]
     b.append(c)
print (b)
