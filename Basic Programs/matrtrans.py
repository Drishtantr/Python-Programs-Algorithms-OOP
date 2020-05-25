def mul(m1):
    m3=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            m3[j][i]=m1[i][j]
    return m3

m1=[[1,2,3],[4,5,6],[6,7,8]]
print(mul(m1))
