def spin(s, n):
    return s[-n:] + s[:-n]

def partner(s, a, b):
    return s.replace(a, 'x').replace(b, 'y').replace('x', b).replace('y', a)

def exchange(s, a, b):
    return partner(s, s[a], s[b])

def dance(s, moves):
    for m in moves:
        if m[0] == 's':
            s = spin(s, int(m[1:]))

        if m[0] == 'x':
            [a, b] = list(map(int, m[1:].split('/')))
            s = exchange(s, a, b)

        if m[0] == 'p':
            s = partner(s, m[1], m[3])

    return s

with open('data.txt', 'r') as f:
    moves = f.read().split(',')

alpha = 'abcdefghijklmnop'
alpha = dance(alpha, moves)

print('Part 1: ', alpha)

i = 1

while alpha != 'abcdefghijklmnop':
    alpha = dance(alpha, moves)
    i += 1

j = 1000000000 % i

for k in range(j):
    alpha = dance(alpha, moves)

print("Part 2: ", alpha)
