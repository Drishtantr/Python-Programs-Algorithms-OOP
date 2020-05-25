def leap(n):
    if(n%4==0):
        if(n%100==0):
            if(n%400==0):
                return "L"
            else:
                return "Not L"
        else:
            return "L"
    else:
        return "not L"

n=int(input())
print (leap(n))

        