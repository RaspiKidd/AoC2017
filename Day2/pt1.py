import numpy as np

ans = 0
data = np.loadtxt ("day2.txt", dtype=int)

for i in range (data.shape[0]):
    ans +=(max(data[i])-min(data[i]))

print (ans)
