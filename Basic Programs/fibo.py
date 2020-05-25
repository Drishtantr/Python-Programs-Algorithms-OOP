n=int(input())
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(n+1):
    temp=a+b
    a=b
    b=temp
    print(b,end=" ")
    if n==b:
        c="yes"
        break
    else:
        c="no"
print(c)