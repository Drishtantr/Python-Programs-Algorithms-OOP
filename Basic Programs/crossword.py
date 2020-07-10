import random
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# puz=np.zeros( (23, 23) )
puz=[]
print(random.choice(alpha))
for i in range(3):
    for j in range(3):
        puz.append(random.choice(alpha))
        # puz[i][j]=random.choice(alpha)
print(puz)

