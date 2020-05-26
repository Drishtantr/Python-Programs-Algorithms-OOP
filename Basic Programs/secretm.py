def pir(s):
    p=s.split(" ")
    new=p
    for i in range(len(p)):
        a=p[i]
        if a.isalnum() is True:
            s=p[i][0]
            p[i]=p[i].replace(p[i][0],"")
            new[i]=p[i]+s+'arg'
        else:
            s=p[i][0]
            p[i]=p[i].replace(p[i][0],"")
            l=p[i][-1]
            p[i]=p[i].replace(p[i][-1],"")
            new[i]=p[i]+s+'arg'+l
    j=" "
    k=j.join(new)
    return k


s="Take what you can, give nothing back."
res=pir(s)
print(res)

