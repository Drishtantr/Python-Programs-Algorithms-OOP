A=[8,2,5,9,6,3,4,7,1]
a=len(A)
for i in range(a-1):
    index=i
    for j in range(i+1,a,1):
        if A[j]<A[index]:
            index=j
    if index!=i:
        temp=A[i]
        A[i]=A[index]
        A[index]=temp

for i in range(a-1):
    print(A[i],end=" ")