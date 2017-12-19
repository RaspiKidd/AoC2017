with open('data.txt', 'r') as f:
    inpt = f.read().split('\n')[:-1]

x = (inpt[0].index('|'))
y = 0

direction = 'd' # down
letters = [] # catching the letters we pass through
currentCase = '|'
steps = 0
while currentCase != ' ':
    steps += 1
    if direction == 'd': # Down
        y += 1
    elif direction == 'u': # up
        y -= 1
    elif direction == 'l': # left
        x -= 1
    elif direction == 'r': # right
        x += 1
    currentCase = inpt[y][x]
    if currentCase == '+':
        if direction in ('d', 'u'):
            if inpt[y][x-1] != ' ':
                direction = 'l'
            else:
                direction = 'r'
        else:
            if inpt[y-1][x] != ' ':
                direction = 'u'
            else:
                direction = 'd'

    elif currentCase not in ('|', '-'):
        letters.append(currentCase)

print(''.join(letters))
print(steps)
