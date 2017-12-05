lines = [line.strip() for line in open ('data.txt', 'r').readlines ()]

jumps = [int (x) for x in lines]
n = len(jumps)
curr = 0

count = 0
while curr >= 0 and curr < n:
    prev = jumps[curr]
    jumps[curr] += 1 if prev < 3 else -1
    curr += prev
    count += 1

print (count)
