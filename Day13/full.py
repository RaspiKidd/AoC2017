with open("data.txt") as f:
    lines = f.readlines()

# Setting up input
n = int(lines[-1].split()[0][:-1]) + 1 # number of walls

depths = [0 for _ in range(n)]
for line in lines:
    index, depth = map(int, line.strip().split(': '))
    depths[index] = int(depth)

# part 1
sumCost = 0
for beat in range(n):
    depth = depths[beat]
    if depth == 0:
        continue
    if (beat % (2 * depth -2)) == 0:
        sumCost += beat * depth
print ('Part 1 - Cost of travel: ', sumCost)

# part 2
startDelay = 0
while True:
    for beat in range(n):
        depth = depths[beat]
        if depth == 0:
            continue
        if ((beat + startDelay) % (depth * 2 - 2)) == 0:
            break
    else: # if not broken during loop
        print('Part 2 - Dealy needed: ', startDelay)
        break
    startDelay += 1
