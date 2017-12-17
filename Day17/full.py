steps = 367

buf = [0]
cur = 0

for i in range (1, 2018):
    cur = ((cur + steps) % len(buf)) + 1
    buf.insert(cur, i)

# part 1 answer
print (buf[buf.index(2017)+1])

for i in range (1, 50000001):
    cur = (cur + steps) % i
    if cur == 0:
        n = i
    cur += 1

# part 2 answer
print (n)
