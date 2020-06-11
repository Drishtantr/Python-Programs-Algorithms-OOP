a='110'
l=0
le=len(a)
co=[]
do=[]
while l<le:
    x=a[l]
    c=1
    d=1
    for i in range(l,len(a)-1,1):
        if x!=a[l+1]:
            l=l+1
            break
        if x=='0':
            c=c+1
            l+=1
        else:
            d=d+1 
            l+=1
    co.append(c)
    do.append(d)
print(co)
print(do)