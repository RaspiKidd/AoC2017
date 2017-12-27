def read():
    with open("data.txt") as f:
        inpt = f.read().splitlines()

    offset = len(inpt) // 2
    infected = set()
    for r, line in enumerate(inpt):
        for c, ch in enumerate(line):
            if ch == '#':
                infected.add((r - offset, c - offset))
    return infected

infected = read()
dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
d = 0
virusAt = (0, 0)

def burst():
    global infected, d, virusAt
    infectionCaused = False
    if virusAt in infected:
        d = (d - 1) % 4
        infected.remove(virusAt)
    else:
        d = (d + 1) % 4
        infected.add(virusAt)
        infectionCaused = True
    virusAt = (virusAt[0] + dirs[d][0], virusAt[1] + dirs[d][1])
    return infectionCaused

numInfections = 0
for i in range(10000):
    if burst():
        numInfections += 1
# Part 1 answer
print(numInfections)

clean = 0
infected = 1
weak = 2
flagged = 3

state = {k: infected for k in read()}
virusAt = (0, 0)

def burst2():
    global state, d, virusAt
    infectionCaused = False
    currentState = state.get(virusAt, 0)
    if currentState == clean:
        d = (d + 1) % 4
        state[virusAt] = weak
    elif currentState == weak:
        state[virusAt] = infected
        infectionCaused = True
    elif currentState == infected:
        d = (d - 1) % 4
        state[virusAt] = flagged
    else: # FLAGGED
        d = (d + 2) % 4
        del state[virusAt]
    virusAt = (virusAt[0] + dirs[d][0], virusAt[1] + dirs[d][1])
    return infectionCaused

numInfections = 0
for i in range(10000000):
    if burst2():
        numInfections += 1
# part 2 answer
print (numInfections)
