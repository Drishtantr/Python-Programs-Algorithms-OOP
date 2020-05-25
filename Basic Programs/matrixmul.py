m1=[[1,2,3],
    [2,3,4],
    [3,4,5]]
m2=[[8,7,6],
    [7,6,5],
    [5,4,3]]
m3=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        for k in range(3):
            m3[i][j]+=m1[i][k]*m2[k][j]
print (m3)