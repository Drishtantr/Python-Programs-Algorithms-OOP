a="abcdefghijklmnop"
n=int(input())
# for i in range(len(a)-1):
#     if i==n-1:
#         a.replace(i,"")
n=n-1
b=a[:n]
c=a[n+1:]
a=b+c
print(a)