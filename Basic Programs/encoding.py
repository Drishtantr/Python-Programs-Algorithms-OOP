x="AAAzzz"
count=0
a=[0,0,0,0,0,0]
c=[0,0,0,0,0,0]
i=0
while (i<len(x)-1):
    a[count]=x[i]
    if a[count]==x[i+1]:
        c[count]+=1
    i+=1
    count+=1

# print(a)
print(c[0],end=" ")
print(a[0],end=" ")

print(c[1],end=" ")
print(a[1],end=" ")