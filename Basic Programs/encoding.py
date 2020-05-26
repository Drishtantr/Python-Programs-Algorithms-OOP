x="AAAAAAzzzz"
a=[]
c=[]
i=0
while (i<len(x)-1):
    # a.append(x[i])
    ca=x.count(x[i])    
    c.append(ca)
    i=ca+1

# print(a)
print(c)