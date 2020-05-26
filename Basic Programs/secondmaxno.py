a=[8,2,5,9,6,3,4,7,1]
c=[0,0,0,0,0,0,0,0,0]
b=max(a)
for i in range(len(a)-1):
    if b!=a[i]:
        c[i]=a[i]
print(max(c))
