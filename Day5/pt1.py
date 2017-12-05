lines = [line.strip() for line in open ('data.txt', 'r').readlines ()]

jumps = [int (x) for x in lines]
n = len (jumps)
curr = 0

count = 0
while curr >= 0 and curr < n:
    jumps[curr] += 1
    curr += jumps[curr] -1
    count += 1

print(count)
