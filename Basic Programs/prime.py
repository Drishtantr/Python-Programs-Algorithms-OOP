def pri(nu):
    c=0
    if (nu>1):
        for i in range(2,nu):
            if (nu%i==0):
                c=1
                break
        if c==1:
            return "Not Prime"
        else:
            return "Prime"
    else:
        return "Prime"
    
    

print("Enter a no ")

nu=int(input())
print (pri(nu))