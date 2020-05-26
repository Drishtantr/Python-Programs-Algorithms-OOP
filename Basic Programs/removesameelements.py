a=[8,2,5,9,6,3,4,7,1,8,2,4,7,6,4]
s=a
for i in range(len(a)-1):
    b=a[i]
    for j in range(i+1,len(a)-1,1):
        if b==a[j]:
            print(a[j])
            # s.remove(a[j])
        else:
            s.remove(b)

# for i in range(len(c)-1):
#     print(c[i])