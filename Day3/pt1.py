input = 289326

total, level = 1, 1

while total < input:
    level +=2
    total = total + level*4 - 4

offset = total - input
steps = offset % (level -1)

print (level -1) / 2 + abs((level / 2) - steps)
