def pr(s):
    p=1
    for i in (range(len(s))):
        a=s[i].isdigit()
        if a is True:
            n=int(s[i])
            p*=n
    return p

s="523hello1"
print(pr(s))