def dist(a):
    if abs(a[1]) > (abs(a[0])*.5):
        return int(abs(a[1])-(abs(a[0])*.5)+abs(a[0]))
    else:
        return int(abs(a[0]))

with open('data.txt') as f:
    inpt = f.readline().strip().split(',')

data = {'n': [0, 1], 's': [0, -1], 'ne': [1, .5],
            'se': [1, -.5], 'nw': [-1, .5], 'sw': [-1, -.5]}
pos = [0, 0]
max = 0

for i in inpt:
    pos[0] += data[i][0]
    pos[1] += data[i][1]
    if max < dist(pos):
        max = dist(pos)


print('Part 1: Current distance away: ' + str(dist(pos)))
print('Part 2: Max distance away: ' + str(max))
