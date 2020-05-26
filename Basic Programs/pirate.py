s="Take what you can, give nothing back."
p=s.split(" ")
# p[1]=p[1].replace(p[1][0],"")
# print(p)
new=p
for i in range(len(p)):
    s=p[i][0]
    p[i]=p[i].replace(p[i][0],"")
    new[i]=p[i]+s+'arg'

j=" "
print(j.join(new))

