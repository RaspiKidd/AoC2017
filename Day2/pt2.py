import numpy as np

ans = 0
data = np.loadtxt ("day2.txt", dtype=int)

for i in range (data.shape [0]):
    for j in range (data.shape[1]):
        cur = data [i][j]
        for k in range (data.shape[1]):
            if k==j or data[i][k]<data[i][j]:
                continue
            if data[i][k]%data[i][j]==0:
                ans+=data[i][k]/data[i][j]
print (ans)
