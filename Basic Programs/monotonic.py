# a=[1,2,3,4,5]
# a=[5,4,3,2,1]
a=[1,5,3,2,0]
c=0
d=0
for i in range(len(a)-1):
    if a[i]>a[i+1]:
        c=c+1
    elif a[i]<a[i+1]:
        d=d+1

if c==4 or d==4:
    print("M")
else:
    print("Not M")