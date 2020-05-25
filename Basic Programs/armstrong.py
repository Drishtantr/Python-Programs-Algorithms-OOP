def ar(n):
    b=n
    sum=0
    while b>0:
        c=b%10
        sum=sum+c**3
        b=b//10
    if sum==n:
        return "A"
    else:
        return "Not A"

n=int(input())
print (ar(n))