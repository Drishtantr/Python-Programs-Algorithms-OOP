A=[8,2,5,9,6,3,4,7,1]
a=int(len(A))
for i in range(a-1):
    print(A[i],end=" ")
print("\n")
for i in range(a-1):
    for j in range (i+1):
        if A[i]<A[j]:
            temp=A[i]
            A[i]=A[j]
            A[j]=temp

for i in range(a-1):
    print(A[i],end=" ")
